═════════════════════════════════════════════════════════════════════════════════
# CHANGELOG
Todas las versiones notables del proyecto Análisis Técnico Bursátil
═════════════════════════════════════════════════════════════════════════════════

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/).
Las versiones van por [Semantic Versioning](https://semver.org/lang/es/).

═════════════════════════════════════════════════════════════════════════════════
[Unreleased]
═════════════════════════════════════════════════════════════════════════════════

### Planeado
- [ ] Screener avanzado (filtros dinámicos)
- [ ] Sistema de alertas automáticas
- [ ] Backtesting de estrategias
- [ ] Mobile app (React Native)
- [ ] Trading automático (broker integration)
- [ ] Análisis de crypto adicionales
- [ ] Sentimiento social (Twitter/Reddit scraping)

═════════════════════════════════════════════════════════════════════════════════
[1.0.0] - 2025-03-15 (PROYECTADO)
═════════════════════════════════════════════════════════════════════════════════

### Added
- ✅ Dashboard principal con tabla interactiva de acciones
- ✅ Sistema de semáforo automático (🟢 BUY / 🟡 HOLD / 🔴 SELL)
- ✅ Análisis detallado por acción (detail view)
- ✅ Gráficos interactivos con Recharts (candlestick + MA)
- ✅ Indicadores técnicos (RSI, MACD, Bollinger Bands, ATR)
- ✅ Portfolio tracker personal
- ✅ Watchlist de acciones favoritas
- ✅ Filtros por mercado (USA / Argentina / MERVAL)
- ✅ API REST completa (FastAPI)
- ✅ Base de datos PostgreSQL con persistencia
- ✅ Autenticación con Supabase Auth
- ✅ Deploy a producción (Vercel + Railway)
- ✅ CI/CD con GitHub Actions
- ✅ Documentación completa (técnica + no-técnica)

### Backend (FastAPI)
```
GET  /api/stocks                    # Lista de acciones + análisis
GET  /api/stocks/:ticker            # Detalle completo de acción
GET  /api/stocks/:ticker/chart      # Datos OHLC para gráfico
GET  /api/stocks/:ticker/indicators # Indicadores técnicos
POST /api/portfolio                 # Agregar posición
GET  /api/portfolio                 # Ver mi portafolio
PATCH /api/portfolio/:ticker        # Editar cantidad
DELETE /api/portfolio/:ticker       # Remover posición
GET  /api/watchlist                 # Ver favoritos
POST /api/watchlist/:ticker         # Agregar favorito
DELETE /api/watchlist/:ticker       # Remover favorito
```

### Frontend (React)
- Dashboard (StockGrid component)
  - Tabla interactiva
  - Filtros por mercado
  - Busca por ticker
  - Columnas: Ticker, Semáforo, Precio, Cambio%, Confianza
  - Responsive (mobile + desktop)

- Detail View (StockDetail component)
  - Gráfico candlestick (7d, 1m, 3m, 1y, all)
  - Moving Averages overlay (MA20, MA50, MA200)
  - Panel de indicadores
  - Recomendación de entrada/salida
  - Botón para agregar a portfolio

- Portfolio Tracker
  - Lista de posiciones
  - P&L por posición
  - % de portafolio
  - Agregar/editar/remover posiciones
  - Resumen total

- Watchlist
  - Guardar acciones favoritas
  - Notificaciones de cambios >5%
  - Quick access desde dashboard

### Styling
- Tema oscuro profesional (Bloomberg-like)
- TailwindCSS completo
- shadcn/ui components
- Colores: Verde (#10b981), Ámbar (#f59e0b), Rojo (#ef4444)
- Responsive: 375px, 768px, 1024px, 1440px

### Indicadores Técnicos
- RSI (14 períodos)
- MACD (12/26/9)
- Bollinger Bands (20/2)
- ATR (14 períodos)
- Moving Averages (20, 50, 200)
- Análisis de volumen

### Scoring Engine
- Ponderación de indicadores
- 30% Tendencia, 25% Momentum, 15% Volatilidad, etc.
- Score 0-100 → Semáforo + Confianza %

### Datos
- Source: yfinance (15-20 min retraso)
- Actualización: Cada 5 minutos (cron job)
- Coverage: 500+ tickers (US + Argentina)
- Histórico: 1 año de datos

### Infrastructure
- Frontend: Vercel
- Backend: Railway
- Database: Supabase PostgreSQL
- CI/CD: GitHub Actions
- Monitoring: Vercel Analytics

### Documentation
- LÉEME.md (non-technical)
- VIBE_CODING_WORKFLOW.md (agentes IA)
- ÍNDICE_GENERAL.md (navegación)
- FORMULARIO_CODESENO_UX_UI.md (UI decisions)
- GALERIA_VISUAL_COMPONENTES.md (visual reference)
- README.md (technical setup)
- CHANGELOG.md (this file)

───────────────────────────────────────────────────────────────────────────────

## [0.2.0] - 2025-03-10 (BETA)

### Added
- Sistema de alertas (email notifications) - FASE BETA
- Screener básico (3 filtros)
- Página individual de acción shareable (/stocks/:ticker)
- Análisis detallado de fundamentales (P/E, EPS, Dividend)
- Backtesting simple (últimos 6 meses)

### Fixed
- Latencia en carga de datos (implementó caché)
- Problema de CORS en API
- Responsive en tablets

### Changed
- Dashboard: Agregó columna "Volumen"
- Detail view: Mejoró UX de gráficos

───────────────────────────────────────────────────────────────────────────────

## [0.1.0] - 2025-03-01 (MVP INICIAL)

### Added
- ✅ TechnicalAnalyzer class (Python)
- ✅ Scoring engine básico (6 indicadores)
- ✅ FastAPI backend con endpoints principales
- ✅ React Dashboard con tabla de acciones
- ✅ Detail view con Recharts
- ✅ Portfolio tracker básico
- ✅ PostgreSQL schema
- ✅ Autenticación básica
- ✅ Deploy en Vercel + Railway

### Indicadores Iniciales
- RSI, MACD, Bollinger Bands, ATR, Volume, MA20/50/200

### Score Engine
- Scoring lineal ponderado
- 50+ points = 🟢, 30-50 = 🟡, <30 = 🔴

### Limitaciones
- Datos con 15-20 min de retraso
- Solo acciones (no crypto ni derivados)
- Base de datos local SQLite en MVP

═════════════════════════════════════════════════════════════════════════════════
## ROADMAP FUTURO (Indicativo, no comprometido)

### v0.2.x (Q2 2025)
- [ ] Screener avanzado (criterios dinámicos)
- [ ] Alertas automáticas (email + push)
- [ ] Backtesting avanzado
- [ ] Análisis fundamental mejorado

### v0.3.x (Q3 2025)
- [ ] Mobile app (PWA o React Native)
- [ ] Crypto adicionales
- [ ] Social sentiment analysis
- [ ] Community features (compartir análisis)

### v1.0.x (Q4 2025)
- [ ] Trading automático (paper trading)
- [ ] Broker integration
- [ ] Options analysis
- [ ] Sistemas personalizados

### v2.0.x (2026)
- [ ] Aplicación mobile nativa
- [ ] Análisis multimercado
- [ ] API pública para terceros
- [ ] Suscripción premium

═════════════════════════════════════════════════════════════════════════════════
## NOTAS DE VERSIÓN FUTURAS (Template)

### [X.X.X] - YYYY-MM-DD

#### Added
- Descripción de nueva feature

#### Changed
- Cambios en features existentes

#### Fixed
- Bug fixes

#### Deprecated
- Features que dejarán de funcionar en futuro

#### Removed
- Features removidas completamente

#### Security
- Cambios relacionados a seguridad

═════════════════════════════════════════════════════════════════════════════════
## CÓMO AGREGAR UN CAMBIO

1. Edita este archivo en tu rama
2. Bajo "Unreleased", agrega tu cambio en la sección apropiada
3. Cuando hagas release, mueve a nueva versión con fecha
4. Sigue formato [Keep a Changelog](https://keepachangelog.com/)

## VERSIONAMIENTO

Usamos [Semantic Versioning](https://semver.org/lang/es/):
- MAJOR.MINOR.PATCH
- MAJOR: Cambios incompatibles (breaking)
- MINOR: Funcionalidad nueva (compatible)
- PATCH: Bug fixes (compatible)

Ejemplos:
- 1.0.0 → 2.0.0: Breaking change (major)
- 1.0.0 → 1.1.0: Nueva feature (minor)
- 1.0.0 → 1.0.1: Bug fix (patch)

═════════════════════════════════════════════════════════════════════════════════
## CONTACTO & FEEDBACK

- Issues: GitHub Issues
- Features: GitHub Discussions
- Bugs: GitHub Issues con label "bug"
- Security: Email privado (no abrir issue)

═════════════════════════════════════════════════════════════════════════════════
Versión: 1.0
Última actualización: Marzo 2025
Mantenedor: Tori @ TORO Holdings
═════════════════════════════════════════════════════════════════════════════════
