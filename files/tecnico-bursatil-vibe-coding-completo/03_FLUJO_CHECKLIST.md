═════════════════════════════════════════════════════════════════════════════════
✅ FLUJO DE EJECUCIÓN & CHECKLIST
═════════════════════════════════════════════════════════════════════════════════

Aquí ves EXACTAMENTE qué ordenes dar a Rosario y qué esperar de cada agente.

═════════════════════════════════════════════════════════════════════════════════
VISIÓN GENERAL: 3 FASES
═════════════════════════════════════════════════════════════════════════════════

FASE 1: BACKEND & ANÁLISIS TÉCNICO (3-4 días)
├─ Agente: Antigravity
├─ Qué hace: Descarga datos, calcula indicadores, genera scores
├─ Resultado: API funcionando que devuelve análisis

FASE 2: FRONTEND & UI (3-4 días)
├─ Agente: Claude Code
├─ Qué hace: Crea componentes bonitos que llaman a la API
├─ Resultado: Dashboard que ves en navegador

FASE 3: DEPLOY & INFRA (1-2 días)
├─ Agente: Antigravity
├─ Qué hace: Pone todo en vivo (Vercel + Railway)
├─ Resultado: App en internet, accesible desde cualquier lado

═════════════════════════════════════════════════════════════════════════════════
FASE 1: BACKEND & ANÁLISIS TÉCNICO
═════════════════════════════════════════════════════════════════════════════════

PASO 1: PEDIR A ROSARIO (Copiar/Pegar)
──────────────────────────────────────

"Rosario, necesito 5 bloques Python para análisis técnico bursátil:

REQUISITOS GENERALES:
- Lenguaje: Python 3.11
- Base de datos: PostgreSQL
- API: FastAPI
- Datos: yfinance

BLOQUE 1: TechnicalAnalyzer
Crea clase que:
- Reciba ticker (ej: AAPL)
- Descargue datos históricos de yfinance (1 año)
- Calcule indicadores: RSI (14), MACD (12/26/9), Bollinger Bands (20/2), ATR (14)
- Devuelva JSON con todos los valores

BLOQUE 2: ScoringEngine
Crea clase que:
- Reciba objeto de indicadores
- Aplique ponderación: 30% Tendencia, 25% Momentum, 15% Volatilidad, etc.
- Calcule score 0-100
- Devuelva signal ('BUY', 'HOLD', 'SELL') + confidence %

BLOQUE 3: FastAPI Endpoints
Crea 3 endpoints:
- GET /api/stocks → lista de 50 tickers con signals
- GET /api/stocks/:ticker → análisis detallado de 1 ticker
- GET /api/stocks/:ticker/chart → datos OHLC últimas 4 semanas

BLOQUE 4: PostgreSQL Schema
Crea 3 tablas:
- stocks (ticker, price, signal, rsi, macd, confidence, updated_at)
- portfolio (user_id, ticker, quantity, cost_base, date_added)
- watchlist (user_id, ticker, added_at)

BLOQUE 5: Cron Job
Crea automación que:
- Cada 5 minutos descargue datos nuevos
- Calcule indicadores
- Actualice tabla 'stocks' en PostgreSQL

Entrega: 5 bloques negros listos para copiar/pegar"


PASO 2: ROSARIO DEVUELVE (Esperas esto)
────────────────────────────────────

5 bloques negros:
1. Clase TechnicalAnalyzer completa
2. Clase ScoringEngine completa
3. 3 endpoints FastAPI
4. SQL para crear las 3 tablas
5. Script de cron job con APScheduler


PASO 3: TÚ COPIAS Y PASAS A ANTIGRAVITY
─────────────────────────────────────────

"Antigravity, aquí 5 bloques Python para integrar:

BLOQUE 1: TechnicalAnalyzer
[COPIAS TODO EL CÓDIGO AQUÍ]
Ubicación: app/analyzers/technical.py

BLOQUE 2: ScoringEngine
[COPIAS TODO EL CÓDIGO AQUÍ]
Ubicación: app/analyzers/scoring.py

BLOQUE 3: Endpoints
[COPIAS TODO EL CÓDIGO AQUÍ]
Ubicación: app/routes/stocks.py

BLOQUE 4: Database Schema
[COPIAS TODO EL CÓDIGO AQUÍ]
Ejecuta en Supabase

BLOQUE 5: Cron Job
[COPIAS TODO EL CÓDIGO AQUÍ]
Ubicación: app/jobs/update_data.py
Ejecuta automáticamente cada 5 min

Intégralos todos. Test: Llama /api/stocks en navegador, debe devolver JSON."


PASO 4: ANTIGRAVITY INTEGRA & REPORTA
──────────────────────────────────────

Antigravity automáticamente:
✓ Crea carpetas necesarias
✓ Integra código en ubicaciones correctas
✓ Verifica imports
✓ Configura variables de entorno
✓ Testa endpoints
✓ Reporta: "Backend integrado ✅"

Qué ves como resultado:
GET http://localhost:8000/api/stocks
```json
{
  "stocks": [
    {
      "ticker": "AAPL",
      "price": 185.50,
      "signal": "BUY",
      "confidence": 72,
      "rsi": 58,
      "macd": "Positivo"
    },
    ...
  ]
}
```

CHECKLIST FASE 1:
[ ] Antigravity: "Backend integrado ✅"
[ ] Llamás /api/stocks → devuelve JSON
[ ] Llamás /api/stocks/AAPL → devuelve análisis
[ ] Datos están frescos (actualizados hace poco)
[ ] Puedes ir a FASE 2

═════════════════════════════════════════════════════════════════════════════════
FASE 2: FRONTEND & UI
═════════════════════════════════════════════════════════════════════════════════

PASO 1: ELEGIR UI EN BIBLIOTECA_UI.md
─────────────────────────────────────

Abre 02_BIBLIOTECA_UI.md y decide:
- Tema (Dark Profesional / Light / Glassmorphism)
- Paleta de colores (Clásica / Moderno / Bank)
- Tipografía (Fintech / Moderno / Luxury)
- Semáforo (Badge / Button / Pill)
- Tabla (Clásica / Cards / Compacta)
- Detail View (Side Panel / Modal / Full Page)
- Portfolio (Resumen / Pie Chart / Cards)

EJEMPLO: "Dark Profesional + Clásica Fintech + Fintech Clásica tipografía
+ Button Prominent semáforo + Tabla Clásica + Side Panel + Resumen Portfolio"


PASO 2: PEDIR A ROSARIO (Copiar/Pegar)
──────────────────────────────────────

"Rosario, necesito 4 componentes React con [TUS ELECCIONES DE BIBLIOTECA_UI]:

BLOQUE 1: StockGrid (Dashboard)
Componente que:
- Renderiza tabla de acciones
- Columnas: Ticker, Semáforo, Precio, Cambio%, Confianza
- Click en fila abre DetailView
- Filtros por mercado (USA / Argentina)
- Busca por ticker
- Responsive mobile + desktop
- [USA ESTILOS DE BIBLIOTECA_UI]

BLOQUE 2: DetailView
Componente que:
- Muestra análisis detallado de 1 acción
- Gráfico candlestick últimas 4 semanas (Recharts)
- Indicadores técnicos (RSI, MACD, BB, ATR)
- Recomendación de entrada/salida
- Botón para agregar a portfolio
- [USA ESTILOS DE BIBLIOTECA_UI]

BLOQUE 3: Portfolio
Componente que:
- Muestra mis posiciones
- P&L por posición
- Total portafolio
- Botón agregar posición
- [USA ESTILOS DE BIBLIOTECA_UI]

BLOQUE 4: Pages Setup
Crea estructura Next.js:
- pages/index.tsx (importa StockGrid)
- pages/stocks/[ticker].tsx (importa DetailView)
- pages/portfolio.tsx (importa Portfolio)
- Configura routing

Entrega: 4 bloques negros React"


PASO 3: TÚ COPIAS Y PASAS A CLAUDE CODE
────────────────────────────────────────

"Claude Code, aquí 4 componentes React:

BLOQUE 1: StockGrid
[CÓDIGO AQUÍ]
Ubicación: src/components/StockGrid.tsx

BLOQUE 2: DetailView
[CÓDIGO AQUÍ]
Ubicación: src/components/DetailView.tsx

BLOQUE 3: Portfolio
[CÓDIGO AQUÍ]
Ubicación: src/components/Portfolio.tsx

BLOQUE 4: Pages
[CÓDIGO AQUÍ]
Ubicación: src/pages/index.tsx, src/pages/stocks/[ticker].tsx, src/pages/portfolio.tsx

Intégralos todos. La API está en http://localhost:8000"


PASO 4: CLAUDE CODE INTEGRA & REPORTA
──────────────────────────────────────

Claude Code automáticamente:
✓ Crea archivos en ubicaciones correctas
✓ Integra imports necesarios
✓ Configura routing
✓ Verifica que no haya errores de sintaxis
✓ Reporta: "Frontend integrado ✅"

Qué ves como resultado:
```bash
npm run dev
http://localhost:3000
→ Dashboard con tabla de stocks, clickeable, bonita
```

CHECKLIST FASE 2:
[ ] Claude Code: "Frontend integrado ✅"
[ ] npm run dev funciona
[ ] Ves dashboard con tabla en http://localhost:3000
[ ] Click en stock abre análisis detallado
[ ] Portfolio tracker muestra posiciones
[ ] Estilos según BIBLIOTECA_UI
[ ] Puedes ir a FASE 3

═════════════════════════════════════════════════════════════════════════════════
FASE 3: DEPLOY & INFRA
═════════════════════════════════════════════════════════════════════════════════

PASO 1: PEDIR A ROSARIO CONFIGURACIÓN
──────────────────────────────────────

"Rosario, necesito 5 bloques de configuración para deploy:

BLOQUE 1: Dockerfile Frontend
Para: Next.js app
Puerto: 3000
Entrypoint: npm start

BLOQUE 2: Dockerfile Backend
Para: FastAPI + Python
Puerto: 8000
Entrypoint: uvicorn main:app --reload

BLOQUE 3: docker-compose.yml
Corre frontend + backend juntos en local

BLOQUE 4: GitHub Actions CI/CD
Workflow que:
- Build automático en cada push
- Test automático
- Deploy a Vercel (frontend)
- Deploy a Railway (backend)

BLOQUE 5: .env.example
Variables de entorno necesarias:
- DATABASE_URL
- API_URL
- JWT_SECRET
- Etc.

Entrega: 5 bloques de configuración"


PASO 2: ROSARIO DEVUELVE
──────────────────────────

5 archivos de configuración listos.


PASO 3: TÚ PASAS A ANTIGRAVITY
──────────────────────────────

"Antigravity, aquí configuración para deploy:

BLOQUE 1: Dockerfile Frontend
[CÓDIGO AQUÍ]
Ubicación: frontend/Dockerfile

BLOQUE 2: Dockerfile Backend
[CÓDIGO AQUÍ]
Ubicación: backend/Dockerfile

BLOQUE 3: docker-compose
[CÓDIGO AQUÍ]
Ubicación: docker-compose.yml

BLOQUE 4: GitHub Actions
[CÓDIGO AQUÍ]
Ubicación: .github/workflows/deploy.yml

BLOQUE 5: .env.example
[CÓDIGO AQUÍ]
Ubicación: .env.example

Deployá a:
- Frontend: Vercel
- Backend: Railway
- Database: Supabase PostgreSQL"


PASO 4: ANTIGRAVITY DEPLOYEA & REPORTA
───────────────────────────────────────

Antigravity automáticamente:
✓ Crea cuentas en Vercel/Railway/Supabase (si no existen)
✓ Conecta repositorio GitHub
✓ Configura variables de entorno
✓ Hace primer deploy
✓ Testa endpoints en producción
✓ Reporta URLs en vivo

RESULTADO:
- Frontend en vivo: https://tuapp.vercel.app
- Backend en vivo: https://tuapp.railway.app
- Database: PostgreSQL en Supabase

CHECKLIST FASE 3:
[ ] Antigravity: "Deploy completado ✅"
[ ] Abres https://tuapp.vercel.app → funciona
[ ] Dashboard muestra datos en vivo
[ ] Clickears → funciona
[ ] Portfolio guarda posiciones
[ ] Datos persisten
[ ] MVP EN VIVO 🎉

═════════════════════════════════════════════════════════════════════════════════
RESUMEN: ÓRDENES A ROSARIO
═════════════════════════════════════════════════════════════════════════════════

FASE 1:
[ ] Orden 1: "Rosario, dame 5 bloques Python para..." (Backend)

FASE 2:
[ ] Orden 2: "Rosario, dame 4 componentes React con..." (Frontend)

FASE 3:
[ ] Orden 3: "Rosario, dame 5 bloques de configuración..." (Deploy)

TOTAL: 3 órdenes a Rosario
RESULTADO FINAL: MVP en vivo

═════════════════════════════════════════════════════════════════════════════════
RESUMEN: ÓRDENES A AGENTES
═════════════════════════════════════════════════════════════════════════════════

FASE 1 - Antigravity:
[ ] "Aquí 5 bloques Python. Intégralos en [ubicaciones]"
[ ] Test: Llama /api/stocks → OK

FASE 2 - Claude Code:
[ ] "Aquí 4 componentes React. Intégralos en [ubicaciones]"
[ ] Test: npm run dev → OK

FASE 3 - Antigravity:
[ ] "Aquí configuración. Deployá a Vercel + Railway + Supabase"
[ ] Test: Abro URL en vivo → OK

═════════════════════════════════════════════════════════════════════════════════
TIMELINE ESTIMADO
═════════════════════════════════════════════════════════════════════════════════

DÍA 1:
[ ] Mañana: Rosario order 1 (Backend) - 2h
[ ] Tarde: Antigravity integra + testa - 2h
[ ] Fin de día: Backend ✅

DÍA 2:
[ ] Mañana: Elige UI en BIBLIOTECA_UI.md - 1h
[ ] Mañana: Rosario orden 2 (Frontend) - 2h
[ ] Tarde: Claude Code integra + testa - 2h
[ ] Fin de día: Frontend ✅

DÍA 3:
[ ] Mañana: Rosario orden 3 (Deploy) - 1h
[ ] Tarde: Antigravity deployea - 1h
[ ] Fin de día: MVP EN VIVO 🎉

TOTAL: 3 DÍAS PARA MVP COMPLETO

═════════════════════════════════════════════════════════════════════════════════
Versión: 1.0
Fecha: Marzo 2025
═════════════════════════════════════════════════════════════════════════════════
