const fs=require('fs');
const htmlPath=process.argv[2]||'index.html';
const src=fs.readFileSync(htmlPath,'utf8');

function extractFunction(name){
  const sig=`function ${name}(`; const p=src.indexOf(sig); if(p<0) throw new Error(`No se encontró ${name}`);
  const b=src.indexOf('{',p); let depth=0, quote=null, esc=false, tplDepth=0;
  for(let i=b;i<src.length;i++){
    const c=src[i], prev=src[i-1];
    if(quote){
      if(esc){esc=false;continue} if(c==='\\'){esc=true;continue}
      if(c===quote){quote=null;continue}
      continue;
    }
    if(c==='"'||c==="'"||c==='`'){quote=c;continue}
    if(c==='{')depth++; else if(c==='}'){depth--; if(depth===0)return src.slice(p,i+1)}
  }
  throw new Error(`Función incompleta ${name}`);
}

const localStorage={_d:{},getItem(k){return this._d[k]??null},setItem(k,v){this._d[k]=String(v)},removeItem(k){delete this._d[k]},clear(){this._d={}}};
global.localStorage=localStorage;
global.safe=s=>String(s??'');
global.toast=()=>{}; global.patientAppointments=()=>{}; global.hide=()=>{}; global.alert=()=>{};
global.show=html=>{global.lastShown=html};
global.current=null; global.active='Inicio'; global.editId=null;
global.MEDICAL_AREAS=["Medicina General","Enfermería","Psicología","Nutrición","Terapia Física","Odontología"];
global.users=[
 {name:'Paciente Demo',email:'paciente@sicm.ec',role:'Paciente'},
 {name:'Carlos Vera',email:'coordinacion@sicm.ec',role:'Coordinación'},
 {name:'Dra. Elena Ruiz',email:'medicina@sicm.ec',role:'Medicina General'},
 {name:'Lic. Ana Torres',email:'enfermeria@sicm.ec',role:'Enfermería'},
 {name:'María Fernández',email:'recepcion@sicm.ec',role:'Recepción y Recaudación'},
 {name:'Ps. Sofía Vega',email:'psicologia@sicm.ec',role:'Psicología'},
 {name:'Lic. Andrea Salazar',email:'nutricion@sicm.ec',role:'Nutrición'},
 {name:'Lic. Miguel Flores',email:'terapia@sicm.ec',role:'Terapia Física'},
 {name:'Od. Luis Ramírez',email:'odontologia@sicm.ec',role:'Odontología'}
];

for(const n of ['records','store','professionalsForArea','patientCatalog','patientHistoryEntries','upsertSharedAppointment','syncPatientAppointment','audit','cancelPatientAppointment','dispatchAutomaticAppointmentNotification','availableSlots','validateCedulaEcuador','preparePaymentItem','autoAssignTurnAfterPayment']){
  global.eval(extractFunction(n));
}

const results=[];
function test(rf,desc,fn,limitMs=null){
  const t=process.hrtime.bigint(); let ok=false, detail='';
  try{const v=fn(); ok=!!v; detail=typeof v==='string'?v:desc}catch(e){detail=e.message}
  const ms=Number(process.hrtime.bigint()-t)/1e6;
  if(limitMs!==null) ok=ok && ms<=limitMs;
  results.push({rf,estado:ok?'PASA':'FALLA',tipo:'verificacion_tecnica',tiempo_ms:+ms.toFixed(3),criterio:desc,detalle:detail});
}

// Datos sintéticos para pruebas reproducibles; no son participantes ni resultados de campo.
const pats=[];for(let i=0;i<20;i++)pats.push({id:1000+i,title:`Paciente ${i}`,status:'Activo',date:new Date().toISOString(),data:{Cédula:String(1000000000+i),Nombres:`Paciente ${i}`,'Fecha de nacimiento':'1990-01-01',Teléfono:'0990000000'}});
pats[7].data.Cédula='1710034065';pats[7].title='Paciente Objetivo';store('Registro de pacientes',pats);
store('Historia clínica general',[{id:9001,title:'Paciente Objetivo',status:'Completado',date:new Date().toISOString(),sourceModule:'Atención medicina general',data:{Paciente:'Paciente Objetivo',Alergias:'Ninguna'}}]);

test('RF-01','Recuperar historia por cédula entre 20 expedientes en <=2000 ms',()=>{const p=patientCatalog().find(x=>x.cedula==='1710034065');return p&&patientHistoryEntries(p.name).length>0},2000);

test('RF-02','Registrar cita y propagarla a agenda/gestión en <=3000 ms',()=>{current=users[0];const x={id:2001,title:current.name,status:'Pendiente',date:new Date().toISOString(),createdBy:current.email,createdByRole:'Paciente',data:{Área:'Medicina General',Profesional:'Dra. Elena Ruiz',Fecha:'2026-09-01',Hora:'09:00',Motivo:'Control'}};syncPatientAppointment(x);return records('Agenda profesional').some(a=>a.id===x.id)&&records('Gestión de citas').some(a=>a.id===x.id)},3000);

test('RF-03','El código de búsqueda global contempla coincidencia por cualquier dato serializado',()=>src.includes('JSON.stringify(x).toLowerCase().includes(q)')&&src.includes('Registro de pacientes'));

test('RF-06','Cancelar cita y propagar estado a módulos relacionados',()=>{current=users[0];const x={id:2100,title:current.name,status:'Pendiente',date:new Date().toISOString(),createdBy:current.email,data:{Área:'Medicina General',Fecha:'2026-09-01',Hora:'10:00'}};store('Mis citas',[x]);store('Agenda profesional',[JSON.parse(JSON.stringify(x))]);store('Gestión de citas',[JSON.parse(JSON.stringify(x))]);store('Pacientes asignados',[JSON.parse(JSON.stringify(x))]);cancelPatientAppointment(2100);return ['Mis citas','Agenda profesional','Gestión de citas','Pacientes asignados'].every(m=>records(m).find(a=>a.id===2100)?.status==='Cancelado')&&src.includes('reprogramPatientAppointment')});

test('RF-10','Existe control de acceso por rol también al navegar por código',()=>src.includes('if(current && !(ACCESS[current.role]||[]).includes(m))')&&src.includes('Acceso no autorizado para este rol'));

test('RF-11','Generar notificación automática al crear/actualizar cita',()=>{current=users[0];localStorage.setItem('sicm_messages','[]');store('Personal y horarios',[{id:1,title:'Dra. Elena Ruiz',status:'Activo',data:{'Nombre completo':'Dra. Elena Ruiz','Área':'Medicina General','Inicio de turno':'08:00','Fin de turno':'17:00','Ausencia o licencia':'Ninguna'}}]);dispatchAutomaticAppointmentNotification({title:'Paciente Demo',data:{Área:'Medicina General',Profesional:'Dra. Elena Ruiz',Fecha:'2026-09-02',Hora:'10:00'}},'creada');return JSON.parse(localStorage.getItem('sicm_messages')).some(m=>m.status==='Notificación automática interna')});

test('RF-12','Auditoría conserva usuario, módulo, elemento y fecha',()=>{current=users[1];audit('PRUEBA','Auditoría','Elemento');const a=records('Auditoría')[0];return a&&a.data.Usuario===current.email&&a.data.Módulo==='Auditoría'&&!!a.date});

store('Configuración',[{id:1,status:'Activo',data:{'Área o rol':'Medicina General','Hora inicial':'09:00','Hora final':'11:00','Cupo máximo':'3'}}]);store('Personal y horarios',[{id:1,title:'Dra. Elena Ruiz',status:'Activo',data:{'Nombre completo':'Dra. Elena Ruiz','Área':'Medicina General','Inicio de turno':'09:00','Fin de turno':'11:00','Ausencia o licencia':'Ninguna'}}]);store('Agenda profesional',[]);
test('RF-13','Calcular horarios disponibles desde configuración y agenda',()=>{const s=availableSlots('Medicina General','2026-09-03');return s.length===3&&s[0].time==='09:00'});
test('RF-17','Recuperar perfil profesional activo por área',()=>professionalsForArea('Medicina General').some(p=>p.name==='Dra. Elena Ruiz'));
store('Agenda profesional',[{id:333,title:'X',status:'Confirmado',data:{Área:'Medicina General',Profesional:'Dra. Elena Ruiz',Fecha:'2026-09-03',Hora:'09:00'}}]);
test('RF-19','Disponibilidad refleja inmediatamente franja ocupada',()=>{const s=availableSlots('Medicina General','2026-09-03');return !s.some(x=>x.time==='09:00')&&s.some(x=>x.time==='09:30')},60000);

let pay={id:4001,title:'Paciente Objetivo',status:'Activo',date:new Date().toISOString(),data:{'Área de atención':'Medicina General',Concepto:'Consulta','Valor total':'100','Monto pagado':'40','Método de pago':'Efectivo'}};
test('RF-21','Generar ID único de comprobante interno y disponer de consulta/impresión',()=>{preparePaymentItem(pay,null);return /^CMP-/.test(pay.data['Comprobante ID'])&&src.includes('function printPaymentReceipt')&&src.includes('window.print()')},5000);
test('RF-22','Pago parcial recalcula saldo y pago total deja saldo en cero',()=>{preparePaymentItem(pay,null);const p=pay.data['Saldo pendiente']==='60.00'&&pay.data['Estado de pago']==='Parcial';pay.data['Monto pagado']='100';preparePaymentItem(pay,pay);return p&&pay.data['Saldo pendiente']==='0.00'&&pay.data['Estado de pago']==='Pagado'},2000);

store('Configuración',[{id:2,status:'Activo',data:{'Área o rol':'Medicina General','Hora inicial':'10:00','Hora final':'11:00','Cupo máximo':'1'}}]);store('Agenda profesional',[]);
test('RF-24','Horario y cupo configurados modifican la disponibilidad usada por agenda',()=>{const s=availableSlots('Medicina General','2026-09-04');return s.length===1&&s[0].time==='10:00'});

test('RF-26','Registro de signos vitales está incluido en sincronización automática hacia historia clínica',()=>src.includes('const clinicalModules=["Signos vitales"')&&src.includes('sourceModule:active')&&src.includes('store("Historia clínica general",history)'));
test('RF-27','Localizar paciente por número de cédula entre 20 expedientes en <=3000 ms',()=>!!patientCatalog().find(x=>x.cedula==='1710034065'),3000);
test('RF-28','Rechazar cédula inválida y aceptar cédula ecuatoriana válida',()=>validateCedulaEcuador('1710034065')&&!validateCedulaEcuador('1234567890')&&src.includes('Cédula y fecha de nacimiento son obligatorias'));
test('RF-30','Restricción clínica por rol está aplicada en navegación y catálogo ACCESS',()=>src.includes('if(current && !(ACCESS[current.role]||[]).includes(m))')&&/Paciente:\s*\[[^\]]*"Historia clínica general"/.test(src)&&!/Paciente:\s*\[[^\]]*"Atención psicológica"/.test(src));

store('Admisión y turnos',[]);current=users[4];
const py={id:5001,title:'Paciente Cobro',date:'2026-09-05T09:00:00',createdBy:current.email,createdByRole:current.role,data:{'Área de atención':'Medicina General','Valor total':'20','Monto pagado':'20','Método de pago':'Efectivo'}};preparePaymentItem(py,null);
let turn1='';
test('RF-33','Cobro por área habilita registro del paciente en admisión/turnos',()=>{turn1=autoAssignTurnAfterPayment(py);return records('Admisión y turnos').some(x=>x.id===5001&&x.data['Área solicitada']==='Medicina General')});
test('RF-34','Generar turno consecutivo automáticamente después del cobro',()=>{const py2={id:5002,title:'Paciente Cobro 2',date:'2026-09-05T09:05:00',createdBy:current.email,createdByRole:current.role,data:{'Área de atención':'Medicina General','Valor total':'20','Monto pagado':'20'}};preparePaymentItem(py2,null);const turn2=autoAssignTurnAfterPayment(py2);return turn1.endsWith('001')&&turn2.endsWith('002')});
test('RF-38','Consulta rápida recupera paciente ya registrado sin reingreso manual',()=>{const p=patientCatalog().find(x=>x.name==='Paciente Objetivo');return !!p&&p.cedula==='1710034065'});

const unique=new Map();for(const r of results)unique.set(r.rf,r.estado);
const pass=[...unique].filter(([,s])=>s==='PASA').map(([rf])=>rf);
const summary={archivo:htmlPath,fecha_ejecucion:new Date().toISOString(),nota:'Pruebas técnicas reproducibles con datos sintéticos. No sustituyen ni modifican las sesiones humanas ya realizadas.',total_pruebas:results.length,rf_must_pasa_tecnicamente:pass.length,rf_pasa:pass,resultados:results};
console.log(JSON.stringify(summary,null,2));
