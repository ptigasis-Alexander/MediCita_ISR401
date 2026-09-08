const TOTAL = 112;
const SCENE_SECONDS = 16;

let running = false;
let paused = false;
let muted = false;
let elapsed = 0;
let sceneIndex = -1;
let timer = null;
let sceneTimers = [];
let fontMode = 0;

const $ = s => document.querySelector(s);

const rows = items => `
<table class="table">
  <thead><tr><th>Paciente</th><th>Identificación</th><th>Turno / cita</th><th>Estado</th><th>Acción</th></tr></thead>
  <tbody>
    ${items.map((x,i)=>`
      <tr>
        <td><b>${x[0]}</b></td>
        <td>${x[1]}</td>
        <td>${x[2]}</td>
        <td><span class="tag ${i===2?'warn':''}">${x[3]}</span></td>
        <td>•••</td>
      </tr>`).join('')}
  </tbody>
</table>`;

const side = (active, role='Administración') => `
<aside class="sidebar">
  <div class="side-brand"><span>S</span> SICM</div>
  ${[
    ['⌂','Inicio'],['♙','Pacientes'],['▣','Citas'],['✚','Historia clínica'],
    ['▤','Recetas'],['◈','Enfermería'],['♢','Reportes'],['⚙','Configuración']
  ].map(n=>`<div class="navitem ${n[1]===active?'active':''}"><b>${n[0]}</b>${n[1]}</div>`).join('')}
  <div class="side-user">● Sesión segura<br><b>${role}</b></div>
</aside>`;

const head = (title, sub, role) => `
<div class="page-head">
  <div><h2>${title}</h2><p>${sub}</p></div>
  <div class="avatar"><i>${role[0]}</i><span><b>${role}</b><br>Centro médico</span></div>
</div>`;

const shell = (active,title,sub,role,body) => `
<div class="shell">${side(active,role)}
<section class="content">${head(title,sub,role)}${body}</section>
</div>`;

const scenes = [
{
  name:'1. Acceso por rol',
  k:'PASO 1 DE 7 · LOGIN',
  title:'Acceso seguro según perfil',
  cursor:[69,58],
  speech:'Primero mostramos el acceso por rol. El prototipo separa las funciones visibles según el perfil del usuario. Para esta defensa usamos únicamente datos ficticios y no abrimos evidencia restringida.',
  render:()=>`
    <div class="login">
      <div class="login-intro">
        <div class="mini-brand"><em>S</em><span><b>SICM</b><br><small>Centro médico inteligente</small></span></div>
        <h1>Inicio de sesión<br>por rol</h1>
        <p>La navegación cambia según las responsabilidades del usuario dentro del centro médico.</p>
        <div class="role-card"><b>Demostración académica</b><span>Datos simulados · Sin credenciales reales</span></div>
      </div>
      <div class="login-form">
        <div class="field"><label>Tipo de usuario</label><div class="fieldbox">Recepción⌄</div></div>
        <div class="field"><label>Usuario</label><div id="userValue" class="fieldbox"></div></div>
        <div class="field"><label>Contraseña</label><div id="passValue" class="fieldbox"></div></div>
        <button class="primary">Ingresar</button>
        <div class="notice">✓ Acceso limitado a funciones autorizadas por rol.</div>
      </div>
    </div>`,
  actions:loginActions
},
{
  name:'2. Recepción',
  k:'PASO 2 DE 7 · RECEPCIÓN',
  title:'Registro, búsqueda y vinculación del paciente',
  cursor:[66,33],
  speech:'En recepción demostramos el registro y la búsqueda del paciente. El personal puede localizarlo por nombre, cédula, pasaporte o teléfono y continuar con la cita o el turno, sin acceder a información clínica que no corresponda a su rol.',
  render:()=>shell(
    'Pacientes','Pacientes','Registro y búsqueda administrativa','Recepción',
    `<div class="role-banner">
       <div><h3>Recepción y admisión</h3><p>Buscar paciente → verificar datos → vincular cita o turno.</p></div>
       <span>Datos simulados</span>
     </div>
     <div class="toolbar">
       <div class="search">⌕ Buscar por nombre, cédula, pasaporte o teléfono</div>
       <button class="btn alt">Filtros</button>
       <button class="btn">+ Registrar paciente</button>
     </div>
     ${rows([
       ['Carlos Mendoza','CI 0917482931','08:30 · Medicina General','En espera'],
       ['María Zambrano','Pasaporte P1234567','09:15 · Psicología','Confirmada'],
       ['José Castillo','CI 0929384712','10:00 · Terapia Física','Pendiente']
     ])}
     <div class="notice">✓ El flujo administrativo mantiene separado el acceso a la historia clínica.</div>`
  )
},
{
  name:'3. Enfermería',
  k:'PASO 3 DE 7 · ENFERMERÍA',
  title:'Signos vitales y valoración inicial',
  cursor:[52,62],
  speech:'Luego pasamos a Enfermería. Aquí se registran signos vitales y la valoración previa a consulta. La versión final incluye frecuencia respiratoria, saturación de oxígeno y notas de enfermería, elementos incorporados después de la validación.',
  render:()=>shell(
    'Enfermería','Valoración de enfermería','Paciente: Carlos Mendoza · Cita 08:30','Enfermería',
    `<div class="role-banner">
       <div><h3>Triage en curso</h3><p>Valoración previa a la atención clínica.</p></div>
       <span>08:17</span>
     </div>
     <div class="card">
       <h3>Signos vitales</h3>
       <div class="panel-form">
         <div class="fake-input">Presión: 120 / 80 mmHg</div>
         <div class="fake-input">Temperatura: 36,7 °C</div>
         <div class="fake-input">Pulso: 76 lpm</div>
         <div class="fake-input">Frecuencia respiratoria: 18 rpm</div>
         <div class="fake-input">Saturación O₂: 98%</div>
         <div class="fake-input">Dolor: 2 / 10</div>
         <div class="fake-input wide">Nota: paciente consciente y orientado; valoración realizada sin novedades.</div>
       </div>
       <div style="text-align:right;margin-top:11px"><button class="btn">Guardar valoración</button></div>
     </div>`
  )
},
{
  name:'4. Atención clínica',
  k:'PASO 4 DE 7 · MEDICINA GENERAL',
  title:'Atención e historia clínica por especialidad',
  cursor:[60,60],
  speech:'En Medicina General mostramos la atención clínica. El profesional consulta la información pertinente, registra motivo, evolución y atención, y trabaja sobre una historia clínica organizada por especialidad. El prototipo no realiza diagnósticos automáticos.',
  render:()=>shell(
    'Historia clínica','Historia clínica electrónica','Paciente: Carlos Mendoza · HC-001248','Medicina general',
    `<div class="tabs">
       <span class="active">Medicina general</span><span>Odontología</span><span>Psicología</span><span>Nutrición</span><span>Terapia física</span>
     </div>
     <div class="card">
       <div class="panel-form">
         <div class="fake-input wide">Motivo de consulta: dolor de garganta y fiebre.</div>
         <div class="fake-input wide">Antecedentes relevantes: registrados en la historia clínica.</div>
         <div class="fake-input wide">Evolución / valoración: información registrada por el profesional autorizado.</div>
         <div class="fake-input wide">Plan de atención: seguimiento según criterio profesional.</div>
       </div>
       <div class="notice">El sistema organiza y registra información; no sustituye el criterio clínico.</div>
       <div style="text-align:right;margin-top:10px"><button class="btn alt">Guardar borrador</button> <button class="btn">Firmar atención</button></div>
     </div>`
  )
},
{
  name:'5. Receta',
  k:'PASO 5 DE 7 · PRESCRIPCIÓN',
  title:'Receta enviada a Enfermería',
  cursor:[70,64],
  speech:'Desde Medicina General u Odontología, un profesional autorizado puede registrar una receta. Al confirmarla, el flujo la envía a Enfermería para su verificación y posterior entrega, manteniendo trazabilidad entre prescripción y suministro.',
  render:()=>shell(
    'Recetas','Nueva receta médica','Paciente: Carlos Mendoza · Datos simulados','Medicina general',
    `<div class="card">
       <h3>Tratamiento farmacológico</h3>
       <div class="med-row"><b>Amoxicilina 500 mg</b><span>Oral · cada 8 h</span><span>7 días</span><span>✎</span></div>
       <div class="med-row"><b>Ibuprofeno 400 mg</b><span>Oral · cada 12 h</span><span>5 días</span><span>✎</span></div>
       <div class="notice">Receta asociada a la atención del paciente.</div>
       <button class="btn" style="width:100%">Firmar y enviar a Enfermería</button>
     </div>`
  )
},
{
  name:'6. Entrega de medicamento',
  k:'PASO 6 DE 7 · ENFERMERÍA',
  title:'Verificación y entrega de medicamentos',
  cursor:[63,58],
  speech:'En Enfermería se recibe la receta, se verifica paciente, medicamento, dosis y cantidad, y después se marca la entrega. Así queda trazabilidad de la prescripción, la dispensación, el responsable y el momento de entrega.',
  render:()=>shell(
    'Recetas','Recetas por entregar','Validación del flujo de medicamentos','Enfermería',
    `<div class="card">
       <h3>RX-2026-0174 · Carlos Mendoza</h3>
       <div class="med-row"><b>Amoxicilina 500 mg</b><span>Cada 8 horas</span><span>21 cápsulas</span><span class="tag">Verificada</span></div>
       <div class="med-row"><b>Ibuprofeno 400 mg</b><span>Cada 12 horas</span><span>10 tabletas</span><span class="tag">Verificada</span></div>
       <div class="notice">✓ Receta recibida desde Medicina General.</div>
       <button class="btn">Marcar medicamento entregado</button>
       <span class="tag info" style="margin-left:8px">Responsable y hora registrados</span>
     </div>`
  )
},
{
  name:'7. Reportes',
  k:'PASO 7 DE 7 · CIERRE',
  title:'Reportes por área y trazabilidad',
  cursor:[59,48],
  speech:'Cerramos con reportes. La demostración consolida indicadores por área y un registro de auditoría. Esto permite explicar que MediCita no es solo una interfaz: conecta procesos, roles, registros y trazabilidad dentro de un mismo flujo demostrable.',
  render:()=>shell(
    'Reportes','Reportes y auditoría','Indicadores consolidados del centro médico','Administración',
    `<div class="stats">
       <div class="stat"><small>Medicina general</small><strong>142</strong><em>atenciones</em></div>
       <div class="stat"><small>Odontología</small><strong>86</strong><em>atenciones</em></div>
       <div class="stat"><small>Enfermería</small><strong>174</strong><em>procedimientos</em></div>
       <div class="stat"><small>Terapia física</small><strong>64</strong><em>sesiones</em></div>
     </div>
     <div class="grid2">
       <div class="card"><h3>Atenciones por área</h3><div class="chart">${[93,77,64,52,48,71,59].map(x=>`<i style="height:${x}%"></i>`).join('')}</div></div>
       <div class="card"><h3>Registro de auditoría</h3>
         ${['Paciente consultado por rol autorizado','Valoración de Enfermería registrada','Receta firmada y enviada','Medicamento marcado como entregado'].map((x,i)=>`<div class="activity"><i>✓</i><span><b>${x}</b><br>Operación simulada · 10:2${i}</span></div>`).join('')}
       </div>
     </div>
     <div class="notice">Fin de la ruta de defensa: Recepción → Enfermería → Atención → Receta → Entrega → Reportes.</div>`
  )
}
];

function clearSceneTimers(){
  sceneTimers.forEach(x=>{clearTimeout(x);clearInterval(x)});
  sceneTimers=[];
}
function later(fn,ms){sceneTimers.push(setTimeout(fn,ms))}
function moveCursor(x,y,click=false){
  const c=$('#cursor');
  c.style.left=x+'%';
  c.style.top=y+'%';
  if(click) later(()=>{
    const fx=$('#clickFx');
    fx.style.left=`calc(${x}% + 3px)`;
    fx.style.top=`calc(${y}% + 5px)`;
    fx.classList.remove('go');
    void fx.offsetWidth;
    fx.classList.add('go');
  },800);
}
function 
  if (s) s.classList.remove('show');
}
function loginActions(){
  const type=(el,text,step)=>{
    let i=0;
    const t=setInterval(()=>{
      if(paused)return;
      el.textContent=text.slice(0,++i);
      if(i>=text.length)clearInterval(t);
    },step);
    sceneTimers.push(t);
  };
  later(()=>{moveCursor(70,47,true);type($('#userValue'),'recepcion.demo',75)},700);
  later(()=>{moveCursor(70,59,true);type($('#passValue'),'••••••••',80)},2400);
  later(()=>{moveCursor(72,70,true);
}
function speak(text){
  if(muted||!('speechSynthesis' in window)) return;
  speechSynthesis.cancel();
  const u=new SpeechSynthesisUtterance(text);
  u.lang='es-ES';
  u.rate=1.08;
  u.pitch=1;
  u.volume=1;
  const voices=speechSynthesis.getVoices();
  u.voice=voices.find(v=>/^es/i.test(v.lang))||null;
  speechSynthesis.speak(u);
}
function showScene(i){
  clearSceneTimers();
  sceneIndex=i;
  const sc=scenes[i], browser=$('#browser');
  browser.classList.add('fade');

  setTimeout(()=>{
    $('#screen').innerHTML=sc.render();
    browser.classList.remove('fade','ken');
    void browser.offsetWidth;
    browser.classList.add('ken');

    $('#sceneName').textContent=sc.name;
    $('#chapterKicker').textContent=sc.k;
    $('#chapterTitle').textContent=sc.title;

    const ch=$('#chapter');
    ch.classList.add('show');
    setTimeout(()=>ch.classList.remove('show'),2600);

    moveCursor(sc.cursor[0],sc.cursor[1]);
    
    later(()=>moveCursor(Math.min(82,sc.cursor[0]+8),Math.min(76,sc.cursor[1]+9),true),4200);

    if(sc.actions) sc.actions();
    speak(sc.speech);
  },350);
}
function fmtTime(sec){
  const f=n=>String(n).padStart(2,'0');
  return `${f(Math.floor(sec/60))}:${f(Math.floor(sec%60))}`;
}
function tick(){
  if(!running||paused)return;
  elapsed=Math.min(TOTAL,elapsed+.25);
  const i=Math.min(scenes.length-1,Math.floor(elapsed/SCENE_SECONDS));
  if(i!==sceneIndex) showScene(i);

  $('#progress').style.width=(elapsed/TOTAL*100)+'%';
  $('#clock').textContent=`${fmtTime(elapsed)} / ${fmtTime(TOTAL)}`;

  if(elapsed>=TOTAL){
    running=false;
    clearInterval(timer);
    $('#pauseBtn').textContent='Reiniciar';
    if('speechSynthesis' in window) speechSynthesis.cancel();
  }
}
function start(){
  if(running)return;
  $('#welcome').classList.add('hidden');
  elapsed=0;
  sceneIndex=-1;
  running=true;
  paused=false;
  $('#pauseBtn').textContent='Pausar';
  tick();
  timer=setInterval(tick,250);
}

$('#startBtn').onclick=start;
$('#pauseBtn').onclick=()=>{
  if(!running){start();return}
  paused=!paused;
  $('#pauseBtn').textContent=paused?'Continuar':'Pausar';
  if('speechSynthesis' in window){
    if(paused)speechSynthesis.pause();
    else speechSynthesis.resume();
  }
};
$('#soundBtn').onclick=()=>{
  muted=!muted;
  $('#soundBtn').textContent=muted?'🔇':'🔊';
  if('speechSynthesis' in window){
    if(muted)speechSynthesis.cancel();
    else speak(scenes[sceneIndex]?.speech||'Narración activada.');
  }
};
$('#fontBtn').onclick=()=>{
  fontMode=(fontMode+1)%3;
  document.body.classList.remove('font-large','font-xlarge');
  if(fontMode===1)document.body.classList.add('font-large');
  if(fontMode===2)document.body.classList.add('font-xlarge');
  $('#fontBtn').textContent=fontMode===0?'A+':fontMode===1?'A++':'A';
};
$('#fullBtn').onclick=()=>document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();
$('#markers').innerHTML=scenes.map(()=>'<i></i>').join('');
window.addEventListener('beforeunload',()=>{if('speechSynthesis' in window)speechSynthesis.cancel()});
