# Problem Diary

**Un pequeño sistema, independiente de la IA que uses, para llevar un diario consultable de los problemas que has resuelto, de modo que tu asistente deje de olvidar.**

Idiomas: [todos los idiomas](../README.md)

## La idea

Si hablas con un asistente de IA a diario, resuelves una y otra vez los mismos tipos de problemas, en muchos dispositivos y proyectos. El asistente no recuerda los detalles y gastas varias peticiones en reconstruir el contexto.

Este proyecto guarda un diario en Markdown sencillo dentro de un repositorio Git. Cuando se resuelve un problema, el asistente escribe una entrada breve: **cuál era el problema, los pasos que realmente funcionaron y la conclusión** (no toda la conversación ni los intentos fallidos). La próxima vez, el asistente lee primero el diario y encuentra la respuesta con menos peticiones.

Es útil si tienes muchos proyectos y dispositivos. Si solo haces preguntas rápidas y puntuales, no lo necesitas.

## Cómo funciona

```
 chat con Claude ──"close and save"──▶ enlace rellenado ──▶ Claude Code en la web ──▶ commit + push
        ▲                                                                                  │
        └──────── Project de Claude (repo de GitHub como conocimiento, pulsa Sync) ◀───────┘
```

- **Escritura:** Claude Code (terminal o web) crea la entrada, ejecuta `git pull`, hace commit y push.
- **Lectura:** el repo se añade a un Project de Claude como conocimiento. Tras cada entrada nueva, pulsa el icono Sync.
- **Sin servidor y sin tokens en el chat.** El diario son solo archivos de tu propio repo, así que funciona con cualquier herramienta que lea Markdown.

## Requisitos

- Tu propio repositorio de GitHub (puede ser privado) creado a partir de esta plantilla.
- Una cuenta Claude Pro, Max o Team (necesaria para Claude Code en la web).
- GitHub conectado en [claude.ai/code](https://claude.ai/code), con la app de Claude autorizada en el repo del diario.
- GitHub conectado a claude.ai (la integración con GitHub) para que un Project pueda leer el repo.
- Para entradas largas creadas desde el chat: ejecución de código y creación de archivos activadas en los ajustes de Claude.

## Configuración

1. Crea un repo **privado** a partir de esta plantilla y clona o sube estos archivos.
2. Conecta GitHub en claude.ai/code y autoriza el repo (da acceso solo a este repo).
3. Crea un **Project** de Claude. En su sección de conocimiento pulsa **+**, elige **GitHub**, selecciona tu repo y los archivos a incluir.
4. Instala la skill de `skill/problem-diary/` y edita su línea `REPO:` con tu `owner/nombre-del-repo`.
5. Anota tus dispositivos en `diario/DEVICES.md`, con un único nombre oficial por dispositivo.

## Uso diario

Cuando se resuelva un problema, dile al asistente **"close and save"**. Según la longitud, se usa uno de tres caminos:

| Situación | Qué ocurre |
|---|---|
| Entrada corta, desde el chat | La skill prepara un enlace `claude.ai/code` con el prompt y el repo ya rellenados. Ábrelo y pulsa Intro. |
| Entrada larga, desde el chat | La skill crea el archivo `.md` con el nombre correcto y te indica la carpeta exacta. Súbelo desde la web de GitHub (*Add file > Upload files*). |
| Ya estás en Claude Code | Escribe el archivo directamente: `git pull`, commit, push. Sin límite de longitud. |

Después pulsa **Sync** en el Project de Claude para que los chats vean la nueva entrada.

## Estructura del repositorio

```
README.md                          índice de los README traducidos
CLAUDE.md                          instrucciones para el agente de código
docs/README.{lang}.md              README en cada idioma
diario/
  DEVICES.md                       nombres oficiales de dispositivos (un nombre por dispositivo)
  _TEMPLATE.md                     plantilla de entrada
  {device-slug}/
    YYYY-MM-DD-short-title.md      un archivo por problema resuelto
skill/problem-diary/               la skill "close and save"
  SKILL.md                         flujo de trabajo y reglas
  scripts/build_link.py            construye el enlace rellenado, comprueba longitud y secretos
  assets/entry-template.md         plantilla usada por la skill (mantener sincronizada con diario/_TEMPLATE.md)
```

Los problemas que no pertenecen a un dispositivo concreto (un sitio web, un servicio compartido) van en `diario/general/`.

## Formato de la entrada

Cada entrada tiene los mismos encabezados fijos, para que grep y la búsqueda con IA funcionen de forma fiable: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, más los opcionales **Do not** y **Related**. El contenido se escribe en tu propio idioma. Consulta `diario/_TEMPLATE.md`.

## Límites y privacidad

- Un enlace lleva la entrada dentro de la URL, así que solo lo usan las entradas cortas. Las más largas usan el archivo.
- Abrir el enlace y pulsar Intro sigue siendo manual: no es totalmente automático y ninguna entrada se guarda sin que la veas.
- Cada entrada guardada inicia una sesión de Claude Code en la web, que cuenta para el uso de tu suscripción.
- Mantén el repo privado. Las entradas describen tus sistemas con detalle.
- **Nunca pongas contraseñas, tokens ni claves en una entrada.** Escribe en su lugar dónde están guardados.
- Todo el repo cuenta para la capacidad de conocimiento del Project. Caben cientos de entradas cortas.
- La sincronización de GitHub en los Projects a veces puede retrasarse o fallar. Si el chat no ve una entrada nueva, pulsa Sync otra vez y comprueba.

## Licencia

Elige una licencia para tu fork (MIT es una opción habitual para un proyecto como este).
