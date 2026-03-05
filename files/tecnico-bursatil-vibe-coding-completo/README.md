═════════════════════════════════════════════════════════════════════════════════
# 📊 Análisis Técnico Bursátil MVP
═════════════════════════════════════════════════════════════════════════════════

Dashboard de análisis técnico automático para acciones de Argentina y USA.

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL (Supabase o local)
- Git

### Installation

```bash
# Clonar repo
git clone <repo-url>
cd tecnico-bursatil

# Frontend
cd frontend
npm install
npm run dev  # http://localhost:3000

# Backend (en otra terminal)
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py  # API en :8000
```

### Enviroment Variables

**Frontend** (`.env.local`):
```
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_SUPABASE_URL=...
NEXT_PUBLIC_SUPABASE_ANON_KEY=...
```

**Backend** (`.env`):
```
DATABASE_URL=postgresql://user:password@host/db
YFINANCE_CACHE_MINUTES=5
JWT_SECRET=your-secret-key
```

## 📁 Project Structure

```
tecnico-bursatil/
├── frontend/                  # Next.js + React
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── pages/            # Next.js pages
│   │   ├── hooks/            # Custom hooks
│   │   └── utils/            # Utilities
│   ├── package.json
│   └── next.config.js
│
├── backend/                   # FastAPI + Python
│   ├── app/
│   │   ├── analyzers/        # TechnicalAnalyzer
│   │   ├── routes/           # API endpoints
│   │   ├── models/           # Pydantic models
│   │   ├── db/               # Database
│   │   └── schemas/          # DB schemas
│   ├── main.py
│   └── requirements.txt
│
├── docs/                      # Documentación
│   ├── LÉEME.md              # Non-technical
│   ├── VIBE_CODING_WORKFLOW.md
│   └── ...
│
└── README.md (this file)
```

## 🏗️ Architecture

### Frontend Stack
- **Framework**: Next.js 14 + React 18
- **Styling**: TailwindCSS + shadcn/ui
- **Charts**: Recharts
- **State**: Zustand
- **Data**: TanStack Query

### Backend Stack
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL (Supabase)
- **Data Analysis**: Pandas + NumPy
- **Data Source**: yfinance

### Deployment
- **Frontend**: Vercel
- **Backend**: Railway
- **Database**: Supabase PostgreSQL
- **CI/CD**: GitHub Actions

## 🤖 Agentes IA

### Claude Code (Frontend)
Escribea componentes React, hooks, utilidades.
Integra con MCP Stitch para GitHub, code execution.

### Antigravity (Backend)
Escribe Python, configura APIs, databases, deploys.
Integra con MCP Stitch para GitHub, terminal, database tools.

## 📊 API Endpoints

### Stocks
```
GET  /api/stocks                    # Lista de acciones
GET  /api/stocks/:ticker            # Detalle + análisis
GET  /api/stocks/:ticker/chart      # Datos para gráfico
GET  /api/stocks/:ticker/indicators # Indicadores técnicos
```

### Portfolio
```
GET    /api/portfolio               # Mi portafolio
POST   /api/portfolio               # Agregar posición
DELETE /api/portfolio/:ticker       # Remover posición
PATCH  /api/portfolio/:ticker       # Editar cantidad
```

### Watchlist
```
GET    /api/watchlist               # Mis favoritos
POST   /api/watchlist/:ticker       # Agregar favorito
DELETE /api/watchlist/:ticker       # Remover favorito
```

## 🧪 Testing

```bash
# Frontend
npm run test

# Backend
pytest

# E2E
npm run test:e2e
```

## 🚀 Deployment

### Vercel (Frontend)
```bash
# Conecta GitHub repo
# Auto-deploy en cada push a main
```

### Railway (Backend)
```bash
# Conecta GitHub repo
# Configure env vars en Railway dashboard
# Auto-deploy en cada push a main
```

### Database (Supabase)
```bash
# Crea proyecto en supabase.com
# Conecta en backend .env
# Migrations corren automáticamente
```

## 📚 Documentation

- **LÉEME.md** - Explicación sin código técnico
- **VIBE_CODING_WORKFLOW.md** - Cómo trabajan los agentes IA
- **ÍNDICE_GENERAL.md** - Guía de navegación completa
- **FORMULARIO_CODESENO_UX_UI.md** - Decisiones de diseño
- **GALERIA_VISUAL_COMPONENTES.md** - Referencias visuales

## 🐛 Troubleshooting

### API connection error
```
Frontend no conecta con backend:
1. Verifica NEXT_PUBLIC_API_URL en .env.local
2. Backend corriendo en puerto correcto (8000)
3. CORS habilitado en FastAPI
```

### Database error
```
PostgreSQL connection failed:
1. Verifica DATABASE_URL es correcto
2. Supabase en línea (dashboard)
3. Credentials son válidos
```

### Build error
```
npm run build falla:
1. npm install limpiador: rm -rf node_modules
2. Instala de nuevo: npm install
3. Verifica Node.js version (18+)
```

## 🎯 Roadmap

- **v0.1.0** - MVP básico (tabla + detail + portfolio)
- **v0.2.0** - Screener avanzado + alertas
- **v0.3.0** - Backtesting de estrategias
- **v1.0.0** - Mobile app + trading automático

## 📄 License

MIT

## 👨‍💻 Contributing

1. Fork repo
2. Crea branch (git checkout -b feature/amazing-feature)
3. Commit cambios (git commit -m 'Add amazing feature')
4. Push (git push origin feature/amazing-feature)
5. Open Pull Request

## 💬 Support

- Issues: GitHub Issues
- Docs: Ver DOCUMENTACIÓN en repositorio
- Questions: LÉEME.md (non-tech) o VIBE_CODING_WORKFLOW.md (tech)

═════════════════════════════════════════════════════════════════════════════════
Versión: 1.0
Última actualización: Marzo 2025
Para: Tori @ TORO Holdings
═════════════════════════════════════════════════════════════════════════════════
