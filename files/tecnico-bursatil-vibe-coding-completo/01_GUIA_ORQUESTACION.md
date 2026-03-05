═════════════════════════════════════════════════════════════════════════════════
🎯 GUÍA DE ORQUESTACIÓN - ANÁLISIS TÉCNICO BURSÁTIL MVP
═════════════════════════════════════════════════════════════════════════════════

FLUJO:
Tori (TÚ) → Rosario (ChatGPT) → Bloque Negro → Claude Code / Antigravity

TÚ no codificas. Tú ordenas, Rosario crea, agentes ejecutan.

═════════════════════════════════════════════════════════════════════════════════
📋 TABLA DE CONTENIDOS
═════════════════════════════════════════════════════════════════════════════════

1. Cómo trabaja este sistema (en 1 minuto)
2. Framework elegido (Stack definitivo)
3. Flujo de ejecución (Tori → Rosario → Agentes)
4. Prompts que usas CON ROSARIO (copiar/pegar)
5. Bloques negros (qué esperas recibir)
6. Checklist de ejecución (por fase)
7. Biblioteca de UI (para Rosario + Tori)
8. Cómo reportar a Rosario si algo no funciona

═════════════════════════════════════════════════════════════════════════════════
1. CÓMO TRABAJA ESTE SISTEMA (1 MINUTO)
═════════════════════════════════════════════════════════════════════════════════

PASO 1: TÚ TIENES UNA NECESIDAD
Ejemplo: "Necesito un componente que muestre tabla de stocks"

PASO 2: TÚ ESCRIBÍS A ROSARIO (En este documento hay prompts listos)
"Rosario, crea componente React que muestre tabla de stocks con: [requisitos]"

PASO 3: ROSARIO DEVUELVE "BLOQUE NEGRO"
Un cuadro de código JavaScript/Python que funciona.
(No entiendes ni lees, solo copias)

PASO 4: TÚ COPIAS EL BLOQUE NEGRO

PASO 5: TÚ LE PASAS AL AGENTE (Claude Code o Antigravity)
"Acá el bloque. Intégralo al proyecto en [ubicación]"

PASO 6: AGENTE EJECUTA
El agente automaticamente:
- Lo integra en la carpeta correcta
- Conecta con otros archivos
- Verifica que no haya errores
- Prueba
- Te dice "Listo ✅"

PASO 7: TÚ LE REPORTAS A ROSARIO
"Agente dice que está listo. Siguiente tarea:"

═════════════════════════════════════════════════════════════════════════════════
2. FRAMEWORK ELEGIDO (STACK DEFINITIVO)
═════════════════════════════════════════════════════════════════════════════════

NOTA: Esto es para ROSARIO, no para vos. Pero lo necesitás para dar órdenes claras.

FRONTEND (Lo que ves en pantalla):
  Tecnología: React 18 + Next.js 14
  Estilos: TailwindCSS + shadcn/ui
  Gráficos: Recharts
  Estado: Zustand
  Datos: TanStack Query
  Hosting: Vercel

Por qué: Rápido, moderno, profesional, fácil de mantener.

BACKEND (El cerebro):
  Tecnología: Python 3.11 + FastAPI
  Base de datos: PostgreSQL (Supabase)
  Análisis: Pandas + NumPy
  Datos: yfinance API
  Hosting: Railway

Por qué: Python es excelente para análisis técnico. FastAPI es rápido.

MCP/SKILLS:
  Central: Stitch (conecta herramientas)
  GitHub: Read/write (código)
  Database: PostgreSQL (datos)
  Terminal: Para ejecutar comandos
  Puedes agregar: Slack, Linear, npm, custom tools

═════════════════════════════════════════════════════════════════════════════════
3. FLUJO DE EJECUCIÓN (TÚ → ROSARIO → AGENTES)
═════════════════════════════════════════════════════════════════════════════════

VISUAL:

┌──────────────┐
│   TÚ (TORI)  │ "Rosario, necesito [X]"
└──────┬───────┘
       │
       ↓
┌──────────────────┐
│ ROSARIO (ChatGPT)│ Crea bloque negro
└──────┬───────────┘
       │
       ↓
    BLOQUE NEGRO (Código listo)
       │
       ├─→ Copias
       │
       ↓
┌────────────────────────┐
│  CLAUDE CODE o         │
│  ANTIGRAVITY (Agentes) │ Integra en proyecto
└────────┬───────────────┘
         │
         ↓
     RESULTADO FUNCIONAL


TIMING:

Tori escribe a Rosario:    2-5 minutos
Rosario genera:            1-3 minutos  
Tú copias:                 30 segundos
Agente integra:            5-10 minutos
Total por feature:         10-20 minutos

═════════════════════════════════════════════════════════════════════════════════
4. PROMPTS QUE USAS CON ROSARIO (COPIAR/PEGAR)
═════════════════════════════════════════════════════════════════════════════════

NOTA: Estos son TEMPLATES. Reemplaza [CORCHETES] con tus detalles.

────────────────────────────────────────────────────────────────────────────────
PROMPT 1: CREAR COMPONENTE REACT FRONTEND
────────────────────────────────────────────────────────────────────────────────

"Rosario, crea un componente React que:

NOMBRE: [StockGrid / DetailView / Portfolio / etc]

FUNCIONALIDAD:
- [Descripción clara de qué hace]
- [Qué datos muestra]
- [Interacciones (clickear, hover, etc)]

REQUISITOS TÉCNICOS:
- Tecnología: React 18 + TypeScript
- Estilos: TailwindCSS (tema oscuro profesional)
- Dependencias: Recharts (si tiene gráficos)
- Exportar como: Componente único (export default)

DISEÑO:
- Responsive: mobile (375px) + desktop (1440px)
- Colores: Verde (#10b981), Ámbar (#f59e0b), Rojo (#ef4444)
- Primario: Azul (#1e40af), Background: Negro (#0f172a)
- Tipografía: Space Mono (títulos), Inter (body)

RESULTADO: Bloque negro listo para copiar/pegar"

────────────────────────────────────────────────────────────────────────────────
PROMPT 2: CREAR FUNCIÓN BACKEND PYTHON
────────────────────────────────────────────────────────────────────────────────

"Rosario, crea una clase/función Python que:

NOMBRE: [TechnicalAnalyzer / ScoringEngine / etc]

FUNCIONALIDAD:
- [Qué hace exactamente]
- [Qué datos recibe como input]
- [Qué devuelve como output]

LIBRERÍAS: pandas, numpy, yfinance, pydantic

RESULTADO: Bloque negro listo para copiar/pegar en FastAPI"

────────────────────────────────────────────────────────────────────────────────
PROMPT 3: CREAR ENDPOINT API
────────────────────────────────────────────────────────────────────────────────

"Rosario, crea un endpoint FastAPI que:

RUTA: [GET/POST /api/stocks / etc]

RECIBE: [Parámetros: ticker, fecha, etc]

DEVUELVE: [JSON con estos campos: precio, RSI, MACD, etc]

CONECTA CON: [TechnicalAnalyzer / Database / etc]

FORMATO: JSON estructurado, manejo de errores básico

RESULTADO: Bloque negro listo para copiar/pegar"

────────────────────────────────────────────────────────────────────────────────
PROMPT 4: CREAR SCHEMA DE BASE DE DATOS
────────────────────────────────────────────────────────────────────────────────

"Rosario, crea schema PostgreSQL que:

TABLA: [stocks / portfolio / watchlist / etc]

CAMPOS:
- [id, ticker, price, signal, confidence, etc]

RELACIONES:
- [Si conecta con otras tablas]

ÍNDICES:
- En campos que se filtran frecuentemente

RESULTADO: SQL listo para ejecutar en Supabase"

────────────────────────────────────────────────────────────────────────────────
PROMPT 5: CREAR CRON JOB / AUTOMATIZACIÓN
────────────────────────────────────────────────────────────────────────────────

"Rosario, crea un cron job que:

TAREA: [Actualizar datos / Calcular semáforos / Limpiar cache / etc]

FRECUENCIA: [Cada 5 minutos / Cada hora / Diariamente]

EJECUTA: [Qué función/script]

LENGUAJE: Python + APScheduler (o similar)

MANEJO DE ERRORES: Logging + alertas si falla

RESULTADO: Bloque negro listo para ejecutar"

────────────────────────────────────────────────────────────────────────────────
PROMPT 6: CREAR FICHERO DE CONFIGURACIÓN (Docker, GitHub Actions, etc)
────────────────────────────────────────────────────────────────────────────────

"Rosario, crea [Dockerfile / docker-compose / .github/workflows/deploy.yml]:

PARA: [Frontend Next.js / Backend FastAPI / CI-CD]

REQUISITOS:
- [Puertos, variables de entorno, volúmenes, etc]

RESULTADO: Bloque negro listo para copiar/pegar"

───────────────────────────────────────────────────────────────────────────────
PROMPT 7: CUANDO ALGO NO FUNCIONA
───────────────────────────────────────────────────────────────────────────────

"Rosario, el agente dice que hay error en [X]:

ERROR: [Copiar error exacto que devolvió agente]

CONTEXTO: [Qué estaba haciendo cuando falló]

AYUDA: Genera bloque nuevo que corrija el error"

═════════════════════════════════════════════════════════════════════════════════
5. BLOQUES NEGROS (QUÉ ESPERAS RECIBIR)
═════════════════════════════════════════════════════════════════════════════════

BLOQUE NEGRO = Cuadro de código que Rosario devuelve

CARACTERÍSTICAS:
✅ Funcional (puedes copiar y listo)
✅ Sin explicación (no lees, solo usas)
✅ Importes necesarios (todo incluido)
✅ Comentarios básicos (qué hace cada parte)
✅ Listo para ejecutar (agente lo integra)

FORMATO:
```python
# ← Comienza bloque
import algo

class MiClase:
    def mi_funcion(self):
        return resultado
# ← Termina bloque
```

O:

```jsx
// ← Comienza bloque
import React from 'react'

const MiComponente = () => {
  return <div>contenido</div>
}

export default MiComponente
// ← Termina bloque
```

CUANDO RECIBAS UN BLOQUE:
1. Identifica dónde comienza y dónde termina
2. Copias TODO (Ctrl+A → Ctrl+C)
3. Se lo pasas al agente: "Aquí bloque, intégralo en [ubicación]"
4. Agente lo hace
5. Listo

═════════════════════════════════════════════════════════════════════════════════
6. CHECKLIST DE EJECUCIÓN (POR FASE)
═════════════════════════════════════════════════════════════════════════════════

FASE 1: BACKEND & ANÁLISIS TÉCNICO
─────────────────────────────────

Agente: Antigravity

Orden a Rosario (copiar/pegar):
"Rosario, dame bloques para:
1. TechnicalAnalyzer (descarga yfinance, calcula RSI/MACD/BB/ATR)
2. ScoringEngine (genera score 0-100 → 🟢/🟡/🔴)
3. FastAPI endpoints (GET /api/stocks, GET /api/stocks/:ticker)
4. PostgreSQL schema (tabla stocks, portfolio, watchlist)
5. Cron job (actualiza datos cada 5 minutos)"

Resultado esperado:
[ ] 5 bloques negros (1 por cada tarea)
[ ] Cada bloque está completo y funcional
[ ] Agente reporta: "Integrado y probado ✅"

Test:
[ ] Llamas /api/stocks en navegador → devuelve JSON
[ ] /api/stocks/AAPL → devuelve análisis con scores


FASE 2: FRONTEND & UI
─────────────────────

Agente: Claude Code

Orden a Rosario:
"Rosario, dame bloques para:
1. Dashboard (tabla de acciones + filtros)
2. DetailView (gráfico + indicadores)
3. Portfolio (mis posiciones)
4. Watchlist (acciones favoritas)
5. Pages setup (Next.js)"

Resultado esperado:
[ ] 5 bloques negros
[ ] Cada uno es componente React standalone
[ ] Agente reporta: "Componentes integrados ✅"

Test:
[ ] npm run dev
[ ] http://localhost:3000
[ ] Ves dashboard con tabla bonita


FASE 3: DEPLOY & INFRA
──────────────────────

Agente: Antigravity

Orden a Rosario:
"Rosario, dame bloques para:
1. Dockerfile (frontend)
2. Dockerfile (backend)
3. docker-compose.yml
4. GitHub Actions (CI/CD)
5. Variables de entorno (.env)"

Resultado esperado:
[ ] 5 bloques de configuración
[ ] Agente reporta: "Deployado a Vercel + Railway ✅"

Test:
[ ] Abres URL en Vercel → funciona
[ ] Abres API en Railway → responde

═════════════════════════════════════════════════════════════════════════════════
7. BIBLIOTECA DE UI (PARA ROSARIO + TÚ)
═════════════════════════════════════════════════════════════════════════════════

CUANDO PIDAS A ROSARIO, ESPECIFICA:

TEMA GENERAL:
[ ] Dark Profesional (Bloomberg-like) ← RECOMENDADO
[ ] Light Minimalista (Robinhood-like)
[ ] Glassmorphism Premium (futurista)

PALETA DE COLORES:
[ ] Clásica Fintech: Verde #10b981, Ámbar #f59e0b, Rojo #ef4444
[ ] Moderno Bold: Cian #06b6d4, Amarillo #eab308, Rojo #f87171
[ ] Professional Bank: Verde #059669, Ámbar #d97706, Rojo #dc2626

TIPOGRAFÍA:
[ ] Fintech Clásica: Space Mono + Inter (RECOMENDADO)
[ ] Moderno Bold: IBM Plex Mono + Poppins
[ ] Luxury: Courier Prime + System Sans

COMPONENTES PRINCIPALES:

Semáforo (Buy/Hold/Sell):
  [ ] Simple Badge (solo emoji)
  [ ] Button Prominent (con texto)
  [ ] Animated Pill (con detalles)

Tabla Principal:
  [ ] Tabla Clásica (denso, muchos datos)
  [ ] Cards Grid (visual, moderno)
  [ ] Tabla Compacta (mobile-friendly)

Detail View:
  [ ] Side Panel (desliza desde lado)
  [ ] Modal Centered (popup centrado)
  [ ] Full Page (navegación completa)

Portfolio:
  [ ] Resumen + Lista (tradicional)
  [ ] Pie Chart + Tabla (visual)
  [ ] Cards Grandes (espacioso)

INSTRUCCIÓN PARA ROSARIO:
"Usa tema [X], paleta [Y], tipografía [Z], semáforo [A], tabla [B], detail [C], portfolio [D]"

═════════════════════════════════════════════════════════════════════════════════
8. CÓMO REPORTAR A ROSARIO SI ALGO NO FUNCIONA
═════════════════════════════════════════════════════════════════════════════════

CUANDO AGENTE DEVUELVE ERROR:

PASO 1: Agente te dice qué falló
Ejemplo: "Error en línea 45: 'RSI' not defined"

PASO 2: TÚ LE PASAS A ROSARIO:
"Rosario, error en bloque [nombre]:
Error: [error exacto]
Línea: [número]
Arregla y dame bloque corregido"

PASO 3: Rosario devuelve bloque arreglado

PASO 4: TÚ LE PASAS AL AGENTE DE NUEVO:
"Aquí bloque corregido. Reintegra."

PASO 5: Agente lo hace

═════════════════════════════════════════════════════════════════════════════════
9. RESUMEN: LO QUE TIENES QUE HACER
═════════════════════════════════════════════════════════════════════════════════

TÚ TIENES QUE:
✅ Leer los prompts de este documento
✅ Copiar prompt y pegarlo en Rosario (con detalles tuyos)
✅ Rosario devuelve bloque negro
✅ Copiar bloque negro
✅ Pasarlo al agente: "Aquí bloque, intégralo"
✅ Agente integra y reporta "Listo"
✅ Reportarle a Rosario: "Agente dice que OK"

NO TIENES QUE:
❌ Entender código
❌ Escribir código
❌ Arreglarlo si falla técnicamente
❌ Saber qué es un "import" o "variable"
❌ Leer documentación técnica

═════════════════════════════════════════════════════════════════════════════════

**Sos orquestador. Rosario es dev. Agentes son ejecutores. Vos solo coordinás.**

═════════════════════════════════════════════════════════════════════════════════
Versión: 1.0 (Tori ↔ Rosario ↔ Agentes)
Fecha: Marzo 2025
═════════════════════════════════════════════════════════════════════════════════
