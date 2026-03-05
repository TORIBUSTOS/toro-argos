═════════════════════════════════════════════════════════════════════════════════
🖥️ WORKFLOW DE PROTOTIPO HTML - SHOWROOM CLICKEABLE
═════════════════════════════════════════════════════════════════════════════════

PROPÓSITO: Un HTML clickeable que simula TODA la UI antes de codificar
NO es el producto final, es el "showroom" para validar decisiones visuales

CRÍTICO: Este paso va AQUÍ en el flujo, no antes, no después.

═════════════════════════════════════════════════════════════════════════════════
1. UBICACIÓN EXACTA EN EL FLUJO
═════════════════════════════════════════════════════════════════════════════════

LÍNEA DE TIEMPO:

DÍA 1: Lees documentos
    ↓
DÍA 2 MAÑANA: Completas FORMULARIO_ESTILO_COMPONENTES
    ↓
DÍA 2 MEDIODÍA: ← ESTÁS AQUÍ → Haces PROTOTIPO HTML
    ↓
DÍA 2 TARDE: Validas prototipo (ves si te late)
    ↓
DÍA 2-3: Pasas prototipo + referencia a Claude Code
    ↓
DÍA 3-5: Claude Code crea componentes React reales
    ↓
DÍA 5-7: Deploy
    ↓
LISTO 🎉

═════════════════════════════════════════════════════════════════════════════════
2. CHECKLIST PRE-PROTOTIPO (Validación)
═════════════════════════════════════════════════════════════════════════════════

ANTES de hacer prototipo, verifica:

[ ] ¿Completaste FORMULARIO_ESTILO_COMPONENTES.md?
    SÍ → Continúa
    NO → Vuelve, completá primero

[ ] ¿Tienes "RESUMEN PARA ROSARIO" del formulario?
    SÍ → Continúa
    NO → Cópialo del formulario, sección 9

[ ] ¿Decidiste TODOS estos elementos?
    [ ] Logo (descripción o referencia)
    [ ] Favicon (igual que logo o diferente)
    [ ] Paleta de colores (al menos 3 colores HEX)
    [ ] Esencia visual (profesional/moderno/etc)
    [ ] Estilo de tarjetas (colores, sombras, efectos)
    [ ] Estilo de botones (colores, hover)
    [ ] Estilo de tabla (alternada o uniforme)
    [ ] Estilo de inputs (borde, focus, error)
    
    Si falta algo → Vuelve a FORMULARIO_ESTILO_COMPONENTES
    Si está todo → Continúa

═════════════════════════════════════════════════════════════════════════════════
3. ORDEN A ROSARIO - PROTOTIPO HTML
═════════════════════════════════════════════════════════════════════════════════

COPIA TODO ESTO Y PÉGALO EN ROSARIO:

───────────────────────────────────────────────────────────────────────────────

Rosario, necesito un PROTOTIPO HTML CLICKEABLE para validar UI.

IMPORTANTE: Este es un "showroom" visual, NO el producto final.
Objetivo: Ver cómo se vería todo junto antes de pasar a React.

PANTALLAS A INCLUIR (4 tabs clickeables):
1. Dashboard - Tabla de stocks
2. Detail - Análisis detallado de 1 acción
3. Portfolio - Mis posiciones
4. Watchlist - Acciones favoritas

PANTALLA 1: DASHBOARD
┌─────────────────────────────────────┐
│ Logo + Nombre del proyecto          │
├─────────────────────────────────────┤
│ [Filtros: USA] [Argentina]          │
├─────────────────────────────────────┤
│ Tabla:                              │
│ TICKER │ SEMÁFORO │ PRECIO │ %CHG   │
│ AAPL   │    🟢    │ $185.50│ +2.3% │
│ GGAL   │    🔴    │ $45.25 │ -3.1% │
│ MERV   │    🟡    │ 2145.30│ -0.8% │
│ (clickeable cada fila)              │
└─────────────────────────────────────┘

PANTALLA 2: DETAIL
┌─────────────────────────────────────┐
│ ← Back | AAPL                       │
├─────────────────────────────────────┤
│ 🟢 BUY - 72% Confianza              │
│ Precio: $185.50 | Cambio: +2.3%     │
│                                     │
│ [Gráfico simulado - línea con área] │
│                                     │
│ Indicadores:                        │
│ RSI: 58 | MACD: Positivo | ATR: 2.45
│                                     │
│ Recomendación:                      │
│ "Compra entre $183-186..."          │
│                                     │
│ [Botón: + Agregar a Portfolio]      │
└─────────────────────────────────────┘

PANTALLA 3: PORTFOLIO
┌─────────────────────────────────────┐
│ Mi Portafolio                       │
├─────────────────────────────────────┤
│ Total: $52,300                      │
│ Ganancia: +$17,300 (+49%) 🟢       │
│                                     │
│ AAPL: 100 acc                       │
│ $18,550 | +$3,550 (+23%) 🟢        │
│                                     │
│ BTC-USD: 0.5 BTC                    │
│ $33,750 | +$13,750 (+69%) 🟢🟢     │
│                                     │
│ [Botón: + Agregar posición]         │
└─────────────────────────────────────┘

PANTALLA 4: WATCHLIST
┌─────────────────────────────────────┐
│ Mis Favoritos                       │
├─────────────────────────────────────┤
│ AAPL  $185.50  +2.3%  [❌ Remover]  │
│ MSFT  $412.30  +1.8%  [❌ Remover]  │
│ TSLA  $245.80  -1.2%  [❌ Remover]  │
│                                     │
│ [Botón: + Agregar a Watchlist]      │
└─────────────────────────────────────┘

ESTILOS (USA EXACTAMENTE ESTO):

[AQUÍ PEGÁS TODO EL "RESUMEN PARA ROSARIO" DE TU FORMULARIO 04]

Ejemplo de cómo vería (reemplaza con TUS valores):
```
ESENCIA VISUAL: Dark Profesional

COLORES PERSONALIZADOS:
- Color 1: #1e40af (Primary - botones)
- Color 2: #10b981 (BUY - verde)
- Color 3: #f59e0b (HOLD - ámbar)
- Color 4: #ef4444 (SELL - rojo)
- Background: #0f172a (negro profundo)
- Cards: #1e293b (gris oscuro)

LOGO: [Tu descripción]

TARJETAS:
- Fondo: #1e293b
- Borde: #1e40af 2px redondeado
- Sombra: Azul sutil
- Hover: Cambio a #3b82f6 + elevate

BOTONES:
- Primary: Fondo #1e40af, Texto blanco
- Hover: Fondo #3b82f6 + glow azul
- Secondary: Fondo #1f2937, Texto #e2e8f0

[Etc., todo lo que respondiste]
```

CARACTERÍSTICAS DEL HTML:
- Single file (todo en 1 archivo)
- 4 tabs clickeables (Navigation simple)
- Responsive (375px mobile - 1440px desktop)
- CSS inline (fácil de editar)
- NO JavaScript complejo
- Colores EXACTOS que especificaste
- Efectos hover según indicaste
- Logo en header (text o placeholder)
- Favicon en pestaña del navegador
- Pueda verse en cualquier navegador

ENTREGA: Un archivo llamado "prototipo-ui.html"
Puede abrirse directamente en navegador (sin servidor)

───────────────────────────────────────────────────────────────────────────────

═════════════════════════════════════════════════════════════════════════════════
4. DESPUÉS QUE ROSARIO DEVUELVE EL HTML
═════════════════════════════════════════════════════════════════════════════════

PASO 1: Rosario te devuelve "prototipo-ui.html" (bloque negro)
┌────────────────────────────────────────┐
│ ```html                                │
│ <!DOCTYPE html>                        │
│ <html>                                 │
│ ...                                    │
│ </html>                                │
│ ```                                    │
└────────────────────────────────────────┘

PASO 2: VOS COPIAS EL BLOQUE NEGRO COMPLETO
- Ctrl+A en el bloque
- Ctrl+C (copiar)

PASO 3: CREAS UN ARCHIVO NUEVO
- Abrís bloc de notas / VS Code / editor simple
- Pegás el código (Ctrl+V)
- Guardás como "prototipo-ui.html"

PASO 4: ABRES EN NAVEGADOR
- Click derecho en "prototipo-ui.html"
- "Abrir con" → Chrome / Firefox / Safari
- ¡VES LA UI CLICKEABLE!

PASO 5: VALIDÁS
[ ] ¿Se ven bien los colores?
[ ] ¿Los botones se ven clicables?
[ ] ¿El hover funciona?
[ ] ¿La tabla se ve clara?
[ ] ¿El logo se ve bien?
[ ] ¿Es responsive (se ve bien en mobile)?
[ ] ¿Te late la esencia visual?

SI TODO SÍ → Continúa a PASO 6
SI ALGO NO → Salta a PASO 7

PASO 6: GUARDÁS REFERENCIA & AVANZAN A REACT
[ ] Guardás "prototipo-ui.html" en una carpeta segura
[ ] Le pasas a Claude Code:

"Aquí prototipo visual de UI (prototipo-ui.html).
Basándote exactamente en ESTE diseño visual,
crea componentes React con ESTOS estilos:

[Pegás el "RESUMEN PARA ROSARIO" del formulario 04]

Ubicaciones:
- src/components/Dashboard.tsx
- src/components/DetailView.tsx
- src/components/Portfolio.tsx
- src/components/Watchlist.tsx
- src/pages/index.tsx (importa todos)"

PASO 7: SI ALGO NO TE LATE
[ ] Anotás qué cambiar (color, tamaño, efecto)
[ ] Le pasas a Rosario:

"Rosario, el prototipo HTML casi está, pero:
- El color de [X] no me gusta, cambiar a [COLOR HEX]
- El hover de [Y] es [PROBLEMA], hacerlo [QUÉ]
- [Otro cambio]

Devuelve prototipo-ui.html actualizado"

[ ] Rosario devuelve HTML actualizado
[ ] Repetís PASO 2-5
[ ] Cuando te late → PASO 6

═════════════════════════════════════════════════════════════════════════════════
5. CHECKLIST: PROTOTIPO HTML COMPLETADO
═════════════════════════════════════════════════════════════════════════════════

VALIDACIÓN ANTES DE PASAR A REACT:

[ ] Tengo archivo "prototipo-ui.html" en mi computadora
[ ] Lo puedo abrir en navegador y ver 4 tabs clickeables
[ ] Dashboard muestra tabla de stocks
[ ] Click en fila abre Detail
[ ] Detail muestra gráfico + indicadores + recomendación
[ ] Botón "Volver" regresa a Dashboard
[ ] Portfolio muestra posiciones + total
[ ] Watchlist muestra favoritos
[ ] Todos los colores son los que especifiqué
[ ] El hover funciona en botones/filas/cards
[ ] Logo se ve bien en header
[ ] Responsive (se ve bien en mobile simulado)
[ ] Me gusta la esencia visual

[ ] PROTOTIPO VALIDADO ✅

═════════════════════════════════════════════════════════════════════════════════
6. TIMING Y DEPENDENCIAS
═════════════════════════════════════════════════════════════════════════════════

DEPENDENCIAS (Qué debes tener antes):
✅ Completado: 04_FORMULARIO_ESTILO_COMPONENTES.md
✅ Completado: "RESUMEN PARA ROSARIO" del formulario

TIMING:
- Rosario genera HTML: 30 min - 1 hora
- Tú abres y validas: 10-15 min
- Cambios (si hay): 15-30 min por ronda

TOTAL PASO: 1-2 horas (máximo)

QUÉ VIENE DESPUÉS:
→ Pasas prototipo + estilos a Claude Code
→ Claude Code crea componentes React reales
→ Integras en proyecto

═════════════════════════════════════════════════════════════════════════════════
7. ERRORES COMUNES (EVITAR)
═════════════════════════════════════════════════════════════════════════════════

❌ ERROR 1: "Hago prototipo antes de completar formulario"
✅ CORRECTO: Completás formulario PRIMERO, prototipo DESPUÉS

❌ ERROR 2: "Rosario, haz prototipo sin especificar colores"
✅ CORRECTO: Pegás "RESUMEN PARA ROSARIO" CON todos los detalles

❌ ERROR 3: "No sé cómo guardar el HTML"
✅ CORRECTO: 
   1. Copia bloque negro (Ctrl+A → Ctrl+C)
   2. Abre bloc de notas
   3. Pega (Ctrl+V)
   4. Guarda como "prototipo-ui.html"
   5. Doble click → Se abre en navegador

❌ ERROR 4: "Prototipo no se ve bien, empiezo de cero"
✅ CORRECTO: Reporta a Rosario qué cambiar, ella actualiza HTML

❌ ERROR 5: "Paso prototipo a Claude Code sin validar primero"
✅ CORRECTO: Validas con checklist ANTES de pasar

═════════════════════════════════════════════════════════════════════════════════
8. RESUMEN EJECUTIVO
═════════════════════════════════════════════════════════════════════════════════

QUÉ ES:
Un HTML clickeable que simula TODA la UI antes de React real.

CUÁNDO HACERLO:
DÍA 2 MEDIODÍA (después de completar formulario visual)

CÓMO HACERLO:
1. Copià orden a Rosario (pegá resumen formulario)
2. Rosario devuelve HTML
3. Vos copias, guardas, abres en navegador
4. Clickeas, validas, ves si te late
5. Si cambios → Reporta a Rosario
6. Si OK → Pasas a Claude Code

POR QUÉ:
- Validas ANTES de codificar (sin sorpresas)
- Ves cómo se vería todo junto
- Pruebas interactividad (hover, clicks)
- Referencia visual exacta para agentes

TIEMPO:
1-2 horas total (incluyendo cambios)

═════════════════════════════════════════════════════════════════════════════════

**SIGUIENTE PASO DESPUÉS DE ESTO:**

Si prototipo está ✅ validado →

Pasás a: 03_FLUJO_CHECKLIST.md → FASE 2 (Frontend con Claude Code)

═════════════════════════════════════════════════════════════════════════════════
Versión: 1.0
Fecha: Marzo 2025
Para: Tori (Control total de UI visual)
═════════════════════════════════════════════════════════════════════════════════
