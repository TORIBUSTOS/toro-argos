═════════════════════════════════════════════════════════════════════════════════
🤖 VIBE CODING WORKFLOW
═════════════════════════════════════════════════════════════════════════════════

FLUJO DE DESARROLLO CON AGENTES IA
Etapas por procesos → Bloques negros → Ejecución automática

Actualizado: Marzo 2025 | Para: Tori @ TORO Holdings

═════════════════════════════════════════════════════════════════════════════════
📋 TABLA DE CONTENIDOS
═════════════════════════════════════════════════════════════════════════════════

1. Qué es Vibe Coding
2. Los agentes IA en este proyecto
3. Flujo general: Tori → Rosario (chatgpt) → Claude Code/Antigravity
4. Las 3 fases de desarrollo (etapas por procesos)
5. Bloques negros: qué son, cómo funcionan
6. Integración MCP + Stitch
7. Ejemplos reales paso a paso
8. Checklist por fase
9. Troubleshooting común

═════════════════════════════════════════════════════════════════════════════════
1. QUÉ ES VIBE CODING
═════════════════════════════════════════════════════════════════════════════════

VIBE CODING = Desarrollo sin escribir "documentación de código"
              Solo: Prompt → Bloque negro → Ejecución

VENTAJAS:
✅ Ahorra tokens (sin documentación innecesaria)
✅ Velocidad máxima (rápido iteración)
✅ Código funcional directo (sin teoría)
✅ Menos overhead (más acción, menos charla)
✅ Flexible (etapas por procesos, no timeline rígido)

CÓMO FUNCIONA:
┌─────────────────────────────────────────────────────────┐
│ Tori escribe prompt en Rosario (describiendo qué hacer) │
│                 ↓                                        │
│ Rosario genera respuesta en "bloque negro" (código)     │
│                 ↓                                        │
│ Tori copia el bloque negro                              │
│                 ↓                                        │
│ Tori pasa a Claude Code / Antigravity                   │
│                 ↓                                        │
│ Agente IA ejecuta con MCP + Skills                      │
│                 ↓                                        │
│ Output: Componente/función/servicio funcional           │
└─────────────────────────────────────────────────────────┘

═════════════════════════════════════════════════════════════════════════════════
2. LOS AGENTES IA EN ESTE PROYECTO
═════════════════════════════════════════════════════════════════════════════════

CLAUDE CODE (Para desarrollo frontend + lógica ligera)
─────────────────────────────────────────────────────
Qué hace:
  • Escribe React components (Dashboard, Detail view, Portfolio)
  • Crea hooks + utilities
  • Configura Next.js pages
  • Integra Recharts para gráficos
  • Setup Tailwind + shadcn/ui

Cuándo interviene:
  • Fase 2: Frontend completo
  • Ajustes de UI basados en FORMULARIO
  • Debugging de componentes

MCP/Skills que usa:
  • GitHub (push code, create branches)
  • Web search (referencias de librerías)
  • Code execution (test components)
  • File operations (crear/editar archivos)


ANTIGRAVITY (Para backend + infra + deploy)
────────────────────────────────────────────
Qué hace:
  • Escribe Python backend (analyzer, scoring engine)
  • Configura FastAPI endpoints
  • Setup PostgreSQL + migrations
  • Configura Docker containers
  • CI/CD pipelines (GitHub Actions)
  • Deploy a producción (Vercel, Railway)

Cuándo interviene:
  • Fase 1: Backend/data pipeline completo
  • Fase 3: Infra + deploy
  • Troubleshooting de producción

MCP/Skills que usa:
  • GitHub (workflow automation)
  • Terminal (ejecutar comandos)
  • Database tools (PostgreSQL)
  • Docker integration
  • Cloud deployment (Railway, Vercel)


STITCH (Conexión MCP central)
──────────────────────────────
Qué es:
  • Model Context Protocol server
  • Central hub para herramientas
  • Permite que Claude Code + Antigravity accedan a recursos externos

Configuración actual:
  • GitHub (read/write code)
  • Database connections (Supabase/PostgreSQL)
  • APIs externas (yfinance para datos bursátiles)
  • File storage (local + cloud)

Conexiones posibles:
  • Slack (notificaciones de progreso)
  • Linear/GitHub Issues (tracking)
  • Vercel (deploy preview)
  • NPM registry (librerías)
  • Custom tools (análisis técnico específico)

═════════════════════════════════════════════════════════════════════════════════
3. FLUJO GENERAL: TORI → Rosario (chatgpt) → CLAUDE CODE/ANTIGRAVITY
═════════════════════════════════════════════════════════════════════════════════

PASO 1: TÚ (TORI) ESCRIBES EL PROMPT EN Rosario (chatgpt)
───────────────────────────────────────────────

Ejemplo:
"Crea un componente React que:
- Muestre tabla de acciones con ticker, precio, semáforo, cambio %
- Clickeable para abrir detail view
- Responsive en mobile (scroll horizontal)
- Use Recharts para mini gráfico en hover
- Estilos TailwindCSS, tema oscuro
- Exportable como código único"

PASO 2: Rosario (chatgpt) RESPONDE CON BLOQUE NEGRO
──────────────────────────────────────────

Output típico:

```jsx
// Aquí comienza el bloque negro:
import React, { useState } from 'react';
import { LineChart, Line, XAxis, YAxis } from 'recharts';

const StockGrid = ({ stocks }) => {
  const [hoveredTicker, setHoveredTicker] = useState(null);
  
  return (
    <div className="overflow-x-auto bg-slate-900">
      <table className="w-full">
        {/* ... código ... */}
      </table>
    </div>
  );
};

export default StockGrid;
```
// FIN del bloque negro

PASO 3: TÚ COPIAS EL BLOQUE NEGRO
──────────────────────────────────

Seleccionas solo el código (no explicación).
Cómo identificar: El código está entre ``` (triple backtick) o dentro de cuadro gris oscuro.

PASO 4: TÚ PASAS A CLAUDE CODE
───────────────────────────────

Opción A: Directamente en Claude Code chat
  1. Abris Claude Code
  2. Pegas bloque negro en chat
  3. Dices: "Integra este código en el proyecto"

Opción B: Pasa archivo a repo
  1. Creas archivo: src/components/StockGrid.tsx
  2. Copias bloque negro adentro
  3. Harás commit (Claude Code lo hace automáticamente)

PASO 5: CLAUDE CODE EJECUTA CON MCP
───────────────────────────────────

Claude Code:
  1. Lee el bloque negro
  2. Accede a MCP Stitch
  3. Valida que sea código React válido
  4. Busca dependencias necesarias (Recharts, Tailwind)
  5. Integra en src/components/
  6. Crea archivo, actualiza imports
  7. Confirma: "Componente integrado ✅"

PASO 6: RESULTADO FUNCIONAL
───────────────────────────

Output en tu repositorio:
  ✅ src/components/StockGrid.tsx (integrado)
  ✅ package.json (dependencias actualizadas si es necesario)
  ✅ Componente importable en otras páginas
  ✅ Listo para usar

═════════════════════════════════════════════════════════════════════════════════
4. LAS 3 FASES DE DESARROLLO (ETAPAS POR PROCESOS)
═════════════════════════════════════════════════════════════════════════════════

NO ES TIMELINE (Semana 1, 2, 3)
ES PROCESOS (Backend → Frontend → Deploy)

Cada proceso es INDEPENDIENTE y puede hacerse en paralelo
pero la lógica es: datos primero, UI después, deploy último

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FASE 1: BACKEND & DATA PIPELINE (Proceso primero)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUIÉN: Antigravity (agente backend)
CUÁNDO: Primero (data pipeline debe estar lista)
QUÉ HACER:

1. TechnicalAnalyzer class (Python)
   ├─ Descarga datos yfinance
   ├─ Calcula indicadores (RSI, MACD, Bollinger, ATR)
   ├─ Genera score del semáforo (0-100)
   └─ Output: JSON estructurado

2. Scoring Engine
   ├─ Lógica de ponderación (30% tendencia, 25% momentum, etc)
   ├─ Determina 🟢 BUY / 🟡 HOLD / 🔴 SELL
   ├─ Confianza %
   └─ Output: Signal + confianza

3. FastAPI Backend
   ├─ GET /api/stocks → lista de acciones
   ├─ GET /api/stocks/:ticker → detail + análisis
   ├─ GET /api/stocks/:ticker/chart → datos para gráfico
   ├─ POST /api/portfolio → agregar posición
   ├─ GET /api/portfolio → mi portafolio
   └─ Output: REST API funcional

4. PostgreSQL + Migrations
   ├─ Tabla: stocks (ticker, price, signal, etc)
   ├─ Tabla: users_portfolio (user_id, ticker, quantity, cost_base)
   ├─ Tabla: watchlist (user_id, ticker)
   └─ Output: Database schema listo

5. Cron jobs + Actualización de datos
   ├─ Ejecuta cada 5 minutos
   ├─ Trae datos nuevos de yfinance
   ├─ Calcula indicadores
   ├─ Actualiza database
   └─ Output: Datos frescos automáticamente

CHECKLIST FASE 1:
[ ] TechnicalAnalyzer funciona con 10 tickers
[ ] Scoring engine produce señales correctas (backtest)
[ ] FastAPI endpoints responden sin errores
[ ] PostgreSQL schema creado
[ ] Cron jobs ejecutándose
[ ] Datos actualizándose automáticamente
[ ] Test: Llamas API → recibes JSON correcto


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FASE 2: FRONTEND & UI COMPONENTS (Proceso segundo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUIÉN: Claude Code (agente frontend)
CUÁNDO: Después de FASE 1 (backend debe existir)
QUÉ HACER:

1. Dashboard Principal
   ├─ Tabla interactiva de acciones
   ├─ Filtros (mercado USA/Argentina)
   ├─ Busca por ticker
   ├─ Click → abre detail panel
   └─ Output: src/components/Dashboard.tsx

2. Detail View
   ├─ Gráfico candlestick (Recharts)
   ├─ Indicadores (RSI, MACD, ATR, Bollinger)
   ├─ Recomendación de entrada/salida
   ├─ Side panel o modal
   └─ Output: src/components/DetailView.tsx

3. Portfolio Tracker
   ├─ Lista mis posiciones
   ├─ P&L actual por posición
   ├─ % de portafolio
   ├─ Agregar/remover posiciones
   └─ Output: src/components/Portfolio.tsx

4. Watchlist
   ├─ Guardar acciones favoritas
   ├─ Notificaciones de cambios >5%
   └─ Output: src/pages/watchlist.tsx

5. Página de acciones individual
   ├─ URL: /stocks/AAPL
   ├─ Todo el análisis técnico
   ├─ Shareable
   └─ Output: src/pages/stocks/[ticker].tsx

6. Styling completo
   ├─ Tema oscuro profesional
   ├─ Responsive (mobile + desktop)
   ├─ TailwindCSS + shadcn/ui
   └─ Según FORMULARIO_CODESENO

CHECKLIST FASE 2:
[ ] Dashboard muestra tabla de stocks
[ ] Click en stock abre detail view
[ ] Charts renderizan correctamente
[ ] Indicadores muestran números reales
[ ] Portfolio tracker agrega/quita posiciones
[ ] Responsive en mobile
[ ] Estilos según FORMULARIO elegido
[ ] Test: Abre en navegador → funciona sin errores


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FASE 3: INFRA & DEPLOYMENT (Proceso tercero)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUIÉN: Antigravity (agente infra)
CUÁNDO: Después de FASE 1 + 2 (todo debe estar funcional)
QUÉ HACER:

1. Autenticación
   ├─ Supabase Auth (simplest)
   ├─ Email + password
   ├─ Google OAuth optional
   └─ Output: Auth middleware en FastAPI

2. Docker Setup
   ├─ Dockerfile frontend (Next.js)
   ├─ Dockerfile backend (FastAPI)
   ├─ docker-compose.yml
   └─ Output: Containers listos para producción

3. CI/CD Pipeline (GitHub Actions)
   ├─ Test automático en cada push
   ├─ Build automático
   ├─ Deploy automático a Vercel/Railway
   └─ Output: .github/workflows/deploy.yml

4. PostgreSQL en Producción
   ├─ Supabase PostgreSQL (free tier OK para MVP)
   ├─ Backups automáticos
   ├─ Connection pooling
   └─ Output: Environment variables configuradas

5. Deploy Frontend (Vercel)
   ├─ Conecta repo GitHub
   ├─ Auto-deploy en cada push a main
   ├─ Environment variables
   └─ Output: APP en vivo en vercel.app

6. Deploy Backend (Railway)
   ├─ Conecta repo GitHub
   ├─ Auto-deploy FastAPI
   ├─ Environment variables
   └─ Output: API en vivo en railway.app

7. Monitoreo + Alertas
   ├─ Vercel Analytics (gratis)
   ├─ Error tracking (Sentry optional)
   ├─ Database monitoring
   └─ Output: Dashboard de salud

CHECKLIST FASE 3:
[ ] Supabase Auth funciona
[ ] Docker builds sin errores
[ ] GitHub Actions workflows creados
[ ] PostgreSQL en Supabase configurado
[ ] Frontend deployado en Vercel
[ ] Backend deployado en Railway
[ ] Dominios + HTTPS funcionando
[ ] Test: Abres URL en producción → funciona


═════════════════════════════════════════════════════════════════════════════════
5. BLOQUES NEGROS: QUÉ SON, CÓMO FUNCIONAN
═════════════════════════════════════════════════════════════════════════════════

QUÉ ES UN BLOQUE NEGRO
─────────────────────

Bloque negro = Cuadro de código que Rosario (chatgpt) genera
                Listo para copiar y pegar
                Sin explicación adicional
                Funcional al 100%

VISUALMENTE:

```python
# ← Comienza bloque negro aquí
import yfinance as yf
import pandas as pd

class TechnicalAnalyzer:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = yf.download(ticker, period="1y")
    
    def calculate_rsi(self):
        # ... código ...
        return rsi
# ← Termina bloque negro aquí
```

CÓMO LOS IDENTIFICAS
────────────────────

1. Están dentro de ``` (triple backtick)
2. A veces en cuadro gris oscuro (depende del cliente)
3. Tienen botón "Copy code" (copiar directamente)
4. NO tienen explicación verbal dentro

CÓMO LOS USAS
─────────────

1. Selecciona el bloque (Ctrl+A dentro del área)
2. Copia (Ctrl+C)
3. Abre archivo / Claude Code
4. Pega (Ctrl+V)
5. Listo

POR QUÉ SON ÚTILES
──────────────────

✅ Ahorra explicación (menos tokens gastados)
✅ Evita copiar parcialmente
✅ Código funcional listo
✅ Rápido iterar (cambiar un bloque a la vez)
✅ Fácil de versionar (cada bloque es una unidad)

═════════════════════════════════════════════════════════════════════════════════
6. INTEGRACIÓN MCP + STITCH
═════════════════════════════════════════════════════════════════════════════════

QUÉ ES STITCH (MCP SERVER)
──────────────────────────

Stitch es tu "control center" para herramientas.
Permite que Claude Code + Antigravity accedan a:
  • GitHub (código)
  • Bases de datos (PostgreSQL)
  • APIs externas (yfinance, APIs de mercado)
  • Servicios en la nube (Vercel, Railway)

CONFIGURACIÓN ACTUAL
────────────────────

Habilitado hoy:
  ✅ GitHub (read/write)
  ✅ PostgreSQL (local + Supabase)
  ✅ File operations (local)
  ✅ Basic terminal commands

Puedes agregar:
  ⭕ Slack (notificaciones de deploy)
  ⭕ Linear/GitHub Issues (tracking de tasks)
  ⭕ Vercel API (preview deployments)
  ⭕ npm registry (package management)
  ⭕ Custom tools (análisis técnico específico)

CÓMO AGREGAR UNA CONEXIÓN NUEVA
───────────────────────────────

Ejemplo: Quiero Slack notifications

1. Ve a MCP_STITCH_CONFIG.md (archivo nuevo)
2. Busca "Slack" en la sección "Available connections"
3. Sigue instrucciones para autorizar
4. Stitch automáticamente habilita Slack
5. Claude Code / Antigravity pueden usar ahora:
   - mcp.send_slack_message()
   - mcp.slack_notify()

═════════════════════════════════════════════════════════════════════════════════
7. EJEMPLOS REALES PASO A PASO
═════════════════════════════════════════════════════════════════════════════════

EJEMPLO 1: CREAR COMPONENTE DASHBOARD
──────────────────────────────────────

PASO 1: TÚ ESCRIBES EL PROMPT EN Rosario (chatgpt)

"Crea un componente React llamado StockGrid que:
- Renderice tabla de acciones (AAPL, GGAL, MERVAL, MSFT)
- Columnas: Ticker, Semáforo (🟢/🟡/🔴), Precio, Cambio%, Confianza
- Clickeable cada fila para abrir detail
- Hover effect suave (highlight + shadow)
- Responsive en mobile
- Usa TailwindCSS tema oscuro
- Exportable como archivo único"

PASO 2: Rosario (chatgpt) RESPONDE

```jsx
import React, { useState } from 'react';

const StockGrid = () => {
  const stocks = [
    { ticker: 'AAPL', signal: 'BUY', price: 185.50, change: 2.3, confidence: 72 },
    // ... más stocks
  ];

  return (
    <div className="min-h-screen bg-slate-900 text-white p-8">
      <table className="w-full">
        <thead>
          <tr className="border-b border-slate-700">
            <th>Ticker</th>
            <th>Semáforo</th>
            <th>Precio</th>
            <th>Cambio%</th>
          </tr>
        </thead>
        <tbody>
          {stocks.map((stock) => (
            <tr key={stock.ticker} className="hover:bg-slate-800 cursor-pointer">
              <td>{stock.ticker}</td>
              <td>{stock.signal === 'BUY' ? '🟢' : '🔴'}</td>
              <td>${stock.price}</td>
              <td>{stock.change}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StockGrid;
```

PASO 3: TÚ COPIAS EL BLOQUE NEGRO

Seleccionas todo el código (Ctrl+A en el bloque)
Copias (Ctrl+C)

PASO 4: TÚ PASAS A CLAUDE CODE

1. Abris Claude Code
2. Pegas en chat:

"Integra este componente React en el proyecto:
[pega código aquí]

Ubicación: src/components/StockGrid.tsx
Importa en: src/pages/index.tsx"

PASO 5: CLAUDE CODE EJECUTA

Claude Code automáticamente:
  ✅ Crea src/components/StockGrid.tsx
  ✅ Pega el bloque negro adentro
  ✅ Verifica sintaxis
  ✅ Actualiza src/pages/index.tsx con import
  ✅ Confirma: "Componente integrado ✅"

PASO 6: RESULTADO

Tu repositorio ahora tiene:
  ✅ src/components/StockGrid.tsx
  ✅ Componente funcional
  ✅ Importado en página principal
  ✅ Listo para usar

PASO 7: VES EN NAVEGADOR

npm run dev
http://localhost:3000 → ves tabla de stocks funcional 🎉


EJEMPLO 2: CREAR BACKEND ANALYZER
──────────────────────────────────

PASO 1: TÚ ESCRIBES EL PROMPT EN Rosario (chatgpt)

"Crea una clase Python TechnicalAnalyzer que:
- Descarga datos de yfinance para un ticker
- Calcula RSI, MACD, Bollinger Bands, ATR
- Genera score 0-100 basado en indicadores
- Retorna JSON con signal (BUY/HOLD/SELL) + confianza
- Usa pandas + numpy
- Incluye docstrings"

PASO 2: Rosario (chatgpt) RESPONDE CON BLOQUE NEGRO

```python
import yfinance as yf
import pandas as pd
import numpy as np
import json

class TechnicalAnalyzer:
    def __init__(self, ticker, period="1y"):
        self.ticker = ticker
        self.data = yf.download(ticker, period=period, progress=False)
    
    def calculate_rsi(self, period=14):
        """Calculate Relative Strength Index"""
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))
    
    def get_signal(self):
        """Generate trading signal"""
        rsi = self.calculate_rsi().iloc[-1]
        score = 0
        
        if rsi < 30:
            score += 20
        elif rsi > 70:
            score -= 10
        
        if score >= 50:
            return {'signal': 'BUY', 'confidence': min(100, score + 20)}
        elif score >= 30:
            return {'signal': 'HOLD', 'confidence': 50}
        else:
            return {'signal': 'SELL', 'confidence': min(100, 100 - score)}

# Test
analyzer = TechnicalAnalyzer('AAPL')
print(json.dumps(analyzer.get_signal(), indent=2))
```

PASO 3: TÚ COPIAS Y PASAS A ANTIGRAVITY

"Integra este analyzer en backend:
[pega bloque]

Ubicación: app/analyzers/technical.py
Usa en: app/routes/stocks.py
Importa en main API"

PASO 4: ANTIGRAVITY EJECUTA

Antigravity automáticamente:
  ✅ Crea app/analyzers/technical.py
  ✅ Pega clase
  ✅ Verifica imports necesarios
  ✅ Integra en fastapi routes
  ✅ Test: llama analyzer → funciona
  ✅ Confirma: "Analyzer integrado ✅"

PASO 5: RESULTADO

API endpoint ahora disponible:
  GET /api/stocks/AAPL/analyze
  → {"signal": "BUY", "confidence": 72}

═════════════════════════════════════════════════════════════════════════════════
8. CHECKLIST POR FASE
═════════════════════════════════════════════════════════════════════════════════

ANTES DE EMPEZAR:
[ ] Leíste VIBE_CODING_WORKFLOW (este documento)
[ ] Entiendes el flujo: Tori → Rosario (chatgpt) → Bloques negros → Agentes
[ ] Sabes qué hace Claude Code (frontend)
[ ] Sabes qué hace Antigravity (backend/infra)
[ ] Tienes MCP Stitch configurado

FASE 1: BACKEND & DATA PIPELINE
[ ] Antigravity crea TechnicalAnalyzer class
[ ] Antigravity crea Scoring engine
[ ] Antigravity crea FastAPI backend
[ ] Antigravity configura PostgreSQL
[ ] Antigravity setea cron jobs
[ ] Test: Llamás /api/stocks → responde JSON
[ ] Test: API devuelve 10+ tickers con signals correctos
[ ] Documentas en ROADMAP_ETAPAS "FASE 1 COMPLETADA"

FASE 2: FRONTEND & UI
[ ] Claude Code crea Dashboard component
[ ] Claude Code crea DetailView component
[ ] Claude Code crea Portfolio tracker
[ ] Claude Code integra charts (Recharts)
[ ] Claude Code aplica estilos según FORMULARIO
[ ] Test: npm run dev → funciona sin errores
[ ] Test: Tabla muestra datos reales de API
[ ] Test: Click en stock → abre detail panel
[ ] Documentas en ROADMAP_ETAPAS "FASE 2 COMPLETADA"

FASE 3: INFRA & DEPLOY
[ ] Antigravity configura Supabase Auth
[ ] Antigravity crea Dockerfiles
[ ] Antigravity setea GitHub Actions CI/CD
[ ] Antigravity deploya frontend a Vercel
[ ] Antigravity deploya backend a Railway
[ ] Test: Abres URL en Vercel → funciona
[ ] Test: API en Railway responde desde navegador
[ ] Documentas en CHANGELOG "v0.1.0 Released"

═════════════════════════════════════════════════════════════════════════════════
9. TROUBLESHOOTING COMÚN
═════════════════════════════════════════════════════════════════════════════════

P: "Generé un bloque negro pero tiene errores cuando lo ejecuto"
R: El bloque está bien, tal vez faltan dependencias:
   1. Revisa error exacto
   2. Comunica a agente: "Archivo X tiene error Y"
   3. Agente arregla bloque
   4. Re-integra

P: "Claude Code dice que necesita MCP para GitHub"
R: Stitch debe estar habilitado:
   1. Abre MCP_STITCH_CONFIG.md
   2. Verifica que GitHub esté ✅ habilitado
   3. Si no, sigue instrucciones para autorizar
   4. Reinicia Claude Code

P: "La API devuelve datos pero el frontend no los muestra"
R: Problema de integración típico:
   1. Verifica que API está corriendo (docker logs)
   2. Verifica URL correcta en frontend (.env)
   3. Verifica CORS headers en FastAPI
   4. Check console.log en navegador para errores

P: "Deploy en Vercel falló"
R: Comúnmente:
   1. Variables de entorno no configuradas → agrega en Vercel dashboard
   2. Build error → revisa logs en Vercel
   3. API endpoint incorrecto → actualiza .env.production
   4. Comunica a Antigravity: "Deploy falló, fix X"

P: "Quiero agregar feature nuevo (screener, alertas, etc)"
R: Vuelta al VIBE CODING:
   1. Escribis prompt en Rosario (chatgpt) describiendo feature
   2. Rosario (chatgpt) devuelve bloque negro
   3. Pasas a agente correspondiente (Claude Code o Antigravity)
   4. Agente integra
   5. Listo

═════════════════════════════════════════════════════════════════════════════════
RESUMEN EJECUTIVO
═════════════════════════════════════════════════════════════════════════════════

VIBE CODING es:
✅ Rápido (sin documentación innecesaria)
✅ Simple (prompt → bloque → ejecución)
✅ Escalable (agregar features es simple)
✅ Económico (ahorro de tokens)

El flujo:
1. Tú escribes qué hacer en Rosario (chatgpt)
2. Copias el bloque negro que devuelve
3. Pasas a agente IA (Claude Code o Antigravity)
4. Agente integra en proyecto
5. Resultado: Feature funcional

Las 3 fases:
1. FASE 1: Backend (Antigravity)
2. FASE 2: Frontend (Claude Code)
3. FASE 3: Deploy (Antigravity)

MCP Stitch es tu central de herramientas
Puedes agregar más conexiones según necesites

═════════════════════════════════════════════════════════════════════════════════

🚀 PRÓXIMO PASO: Lees BLOQUES_NEGROS_FASE1.md para el primer bloque a ejecutar.

═════════════════════════════════════════════════════════════════════════════════
Versión: 1.0
Fecha: Marzo 2025
Para: Tori @ TORO Holdings
═════════════════════════════════════════════════════════════════════════════════
