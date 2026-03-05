# TORO — Arquitectura + Stack (v0.1)
**Contexto:** PRD TORO — Producto MVP 6  
**Objetivo de este documento:** que Tori pueda “ver el sistema completo” sin tener que sostenerlo en la cabeza.

---

## 0) Documentos base (fuente de este mapa)

Estos documentos ya existen en el ZIP y se toman como referencia de trabajo:

- `VIBE_CODING_WORKFLOW.md` (metodología: roles + agentes + bloques negros)
- `01_GUIA_ORQUESTACION.md` (stack definitivo + flujo operativo)
- `03_FLUJO_CHECKLIST.md` (checklist por fases y entregables)
- `05_WORKFLOW_PROTOTIPO_HTML.md` (proceso de prototipado UI en HTML)
- `02_BIBLIOTECA_UI.md` / `GALERIA_VISUAL_COMPONENTES.md` (referencia visual)
- `FORMULARIO_CODESENO_UX_UI.md` / `04_FORMULARIO_ESTILO_COMPONENTES.md` (inputs de diseño)
- `QUICKSTART_CODIGO_MVP.md` (arranque técnico)

---

## 1) Principio rector
**Separación estricta por capas:**

- **Datos** (market data)
- **Inteligencia** (indicadores + scoring + señal)
- **Interfaz** (dashboard + detalle + watchlist + portfolio)

Esto permite escalar sin reescribir todo.

---

## 2) Stack (definición de MVP)

### Frontend
- **React 18 + Next.js 14**
- **TailwindCSS + shadcn/ui**
- **Recharts** (gráficos/tableros)
- **Zustand** (estado UI)
- **TanStack Query** (fetch/cache de API)
- Deploy: **Vercel**

### Backend
- **Python 3.11 + FastAPI**
- **Pandas + NumPy** (cálculo)
- Indicadores: `pandas-ta` (sugerido) o `ta` (alternativas)
- Base de datos: **PostgreSQL** (ideal: **Supabase**)
- Jobs/cron: **APScheduler** (MVP)
- Deploy: **Railway**

### Datos de mercado
- **Finnhub** (principal, por disponibilidad)
- Alternativas: Yahoo Finance / Alpha Vantage / Polygon (futuro / fallback)

---

## 3) Arquitectura lógica del sistema (visión “de arriba”)

```text
                 ┌──────────────────────────────┐
                 │   UNIVERSO DE ACTIVOS        │
                 │  - CEDEARs subyacentes (filtrados por liquidez)
                 │  - BYMA: MERVAL + Panel General (con filtro opcional)
                 └───────────────┬──────────────┘
                                 │
                                 v
┌───────────────────────────────────────────────────────────────────────┐
│                          MARKET DATA LAYER                            │
│  Finnhub -> OHLCV históricos + precio actual                          │
└──────────────────────────────┬────────────────────────────────────────┘
                               │
                               v
┌───────────────────────────────────────────────────────────────────────┐
│                       ANALYTICS / INTELLIGENCE                        │
│  1) Indicators Engine: RSI, MACD, MA50, MA200, ATR, Volumen, Momentum  │
│  2) Scoring Engine (0..100)                                            │
│  3) Signal Mapper: SELL / HOLD / BUY + confidence                      │
└──────────────────────────────┬────────────────────────────────────────┘
                               │
                               v
┌───────────────────────────────────────────────────────────────────────┐
│                         STORAGE / HISTORY                             │
│  PostgreSQL (Supabase):                                                │
│   - stocks (último estado + métricas)                                  │
│   - stock_history (opcional MVP)                                       │
│   - watchlist (por usuario)                                            │
│   - portfolio (por usuario)                                            │
└──────────────────────────────┬────────────────────────────────────────┘
                               │
                               v
┌───────────────────────────────────────────────────────────────────────┐
│                                 API                                   │
│  FastAPI:                                                              │
│   - GET /api/stocks                                                    │
│   - GET /api/stocks/{ticker}                                           │
│   - GET /api/stocks/{ticker}/chart                                     │
│   - POST /api/watchlist                                                │
│   - POST /api/portfolio                                                │
└──────────────────────────────┬────────────────────────────────────────┘
                               │
                               v
┌───────────────────────────────────────────────────────────────────────┐
│                                 UI                                    │
│  Next.js (Dashboard + Detail + Watchlist + Portfolio)                  │
│  - Radar (tabla + filtros + ranking)                                   │
│  - Gauge semáforo (rojo->amarillo->verde)                              │
│  - Vista por activo (indicadores + señal + gráfico)                    │
└───────────────────────────────────────────────────────────────────────┘
```

---

## 4) Arquitectura física (repositorio sugerido)

> Nota: esto define “dónde vive cada cosa” y reduce caos.

### Backend (FastAPI)
```text
backend/
  app/
    main.py
    core/            # config, settings, env
    data/            # fetchers (Finnhub)
    analyzers/       # indicadores + scoring
      indicators.py
      scoring.py
    routes/
      stocks.py
      watchlist.py
      portfolio.py
    jobs/
      update_data.py # cron APScheduler
    db/
      models.py
      schema.sql
      session.py
```

### Frontend (Next.js)
```text
frontend/
  app/                 # App Router
    page.tsx           # Dashboard
    stocks/[ticker]/page.tsx
    watchlist/page.tsx
    portfolio/page.tsx
  components/
    RadarTable.tsx
    SignalGauge.tsx
    StockChart.tsx
    IndicatorsPanel.tsx
  lib/
    api.ts             # client fetch
    types.ts
    store.ts           # zustand
```

---

## 5) UI: participación activa de Tori (proceso oficial)

**Regla:** no se implementa UI definitiva sin prototipo visual aprobado.

### Paso A — Prototipo HTML
- Rosario genera un **HTML estático** con layout y componentes.
- Tori lo abre, lo mira, y marca cambios.

### Paso B — Formulario UX/UI
Se usa el formulario para que Tori pueda “pedir features” sin leer código:
- Watchlist (sí/no)
- filtros del radar
- qué columnas mostrar
- cómo se ve el semáforo
- qué paneles aparecen en el detalle
- qué atajos de interacción existen

### Paso C — Implementación React
Solo cuando el HTML queda aprobado:
- Claude Code replica la UI en Next.js
- se conectan endpoints reales
- se valida consistencia visual

---

## 6) Cadencia de construcción (fases)

### Fase 1 — Backend + motor
- Market data fetch (Finnhub)
- Indicators + scoring + signal
- API endpoints
- Persistencia en PostgreSQL
- Job scheduler

### Fase 2 — UI (sobre API real)
- Dashboard Radar
- Detail view por ticker
- Watchlist
- Portfolio

### Fase 3 — Deploy + auth
- Supabase Auth (si se decide)
- Railway + Vercel
- variables de entorno
- monitoreo mínimo

---

## 7) Riesgos técnicos (y cómo los mitigamos)

- **Liquidez / activos ilíquidos:** filtro de volumen (PRD sección 11)
- **API rate limits (Finnhub):** cache + batch + refresh diario (MVP)
- **Diferencias CEDEAR vs subyacente:** analizamos subyacente y mostramos “CEDEAR disponible”
- **Complejidad de UI:** prototipo HTML primero (control por Tori)

---

## 8) Entregables próximos (para mantener el mapa visible)

1. `SYSTEM_ARCHITECTURE_MAP.md` (este documento, ya)
2. `DATA_MODEL.md` (tablas + campos + índices)
3. `SCORING_MODEL.md` (fórmula exacta del score 0..100)
4. `UI_PROTOTYPE_DASHBOARD.html` (primer layout del radar)
