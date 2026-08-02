#!/usr/bin/env sh
set -eu

# Ejecutar desde la raíz del repositorio después de descargar todos los archivos.
# Incluye imágenes, audio, video, PDF y partes de archivos 7z.
find . -type f \
  ! -path './.git/*' \
  ! -path './checksums.sha256' \
  \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' \
     -o -iname '*.gif' -o -iname '*.svg' -o -iname '*.webp' \
     -o -iname '*.mp4' -o -iname '*.mov' -o -iname '*.avi' \
     -o -iname '*.mkv' -o -iname '*.mp3' -o -iname '*.wav' \
     -o -iname '*.m4a' -o -iname '*.ogg' -o -iname '*.flac' \
     -o -iname '*.pdf' -o -iname '*.7z' -o -iname '*.7z.*' \) \
  -print0 | sort -z | xargs -0 sha256sum > checksums.sha256

printf '%s\n' 'checksums.sha256 generado correctamente.'
printf '%s\n' 'Verificación: sha256sum --check checksums.sha256'
