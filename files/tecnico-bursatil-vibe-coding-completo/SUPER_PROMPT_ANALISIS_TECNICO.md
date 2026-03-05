# 🎯 SUPER PROMPT: MVP ANÁLISIS TÉCNICO BURSÁTIL
## Dashboard Professional-Grade | Acciones Argentina + Estados Unidos

---

## 📋 CONTEXTO EJECUTIVO

**Objetivo**: Crear un **MVP de análisis técnico profesional** que permita:
- 📊 Visualizar análisis técnico de acciones (MERVAL + NYSE/NASDAQ)
- 🚦 Semáforo automático (Buy/Hold/Sell) basado en indicadores
- 📈 Dashboards interactivos con charts en tiempo real
- 🔍 Métricas técnicas, fundamentales y de sentimiento
- 💾 Persistencia de portafolios y alertas

**Usuario**: Trader/inversionista argentino con interés en mercados locales e internacionales
**Restricción técnica**: MVP funcional en 2-3 semanas

---

## 🏗️ ARQUITECTURA RECOMENDADA

### **Frontend Stack**
```
Framework: React 18 + Next.js 14 (App Router)
Styling: TailwindCSS + shadcn/ui
Charts: Recharts (interactivo, ligero)
State: Zustand (ligero vs Redux)
Data Fetching: TanStack Query (caché inteligente)
Realtime: WebSocket optional (para fase 2)
```

### **Backend Stack**
```
Runtime: Node.js 18+ con Fastify o Express
Data Source: yfinance (Python async) o node-fetch a APIs públicas
Database: PostgreSQL (Supabase) o SQLite local
Cache: Redis (optional para MVP)
Deploy: Vercel (frontend) + Railway/Render (backend)
```

### **Data Pipeline**
```
1. Extractor: Python script con yfinance → PostgreSQL
2. Processor: Cálculo de indicadores (RSI, MACD, BB, ATR)
3. Aggregator: Scoring automático (semáforo 🔴🟡🟢)
4. API: REST endpoint para frontend (cached)
```

---

## 📊 FEATURES MVP (Phase 1)

### **Dashboard Principal**
```
┌─────────────────────────────────────────┐
│  TÉCNICO BURSÁTIL | Mercado: MERVAL/US │
├─────────────────────────────────────────┤
│                                         │
│  🔴 FILTRO: Mercado | Riesgo | Tendencia
│                                         │
│  ┌──────────────────┬─────────────────┐
│  │ Ticker │ Semáforo │ Precio │ Cambio%
│  ├──────────────────┼─────────────────┤
│  │ AAPL   │    🟢    │ $185  │  +2.3%  │
│  │ MERVAL │    🟡    │ 2145  │  -0.8%  │
│  │ GGAL   │    🔴    │ $45   │  -3.1%  │
│  └──────────────────┴─────────────────┘
│
│  [CLICK TICKET → DETAIL VIEW]
```

### **Detail View (Individual Stock)**
```
┌─────────────────────────────────────────┐
│  APPLE (AAPL) | Precio: $185.50         │
├─────────────────────────────────────────┤
│                                         │
│  🟢 SEMÁFORO: BUY (Confianza: 72%)     │
│                                         │
│  📈 GRÁFICO (7 días | 1 mes | 3m | 1y) │
│  [Chart candlestick + moving averages]  │
│                                         │
│  📊 INDICADORES TÉCNICOS               │
│  ├─ RSI: 58 (neutral)                  │
│  ├─ MACD: Cruce alcista                │
│  ├─ BB: Precio en banda media          │
│  ├─ ATR: $2.45 (volatilidad)           │
│  └─ Volume: +15% promedio              │
│                                         │
│  💰 FUNDAMENTALES                       │
│  ├─ P/E: 28x                           │
│  ├─ EPS Grow: +12% YoY                 │
│  ├─ Dividend: 0.24% yield              │
│  └─ Market Cap: $2.8T                  │
│                                         │
│  📌 RECOMENDACIÓN                       │
│  "Compra en tendencia alcista, esperar │
│   confirmación en soporte de $183"      │
│                                         │
│  [+ AGREGAR A PORTAFOLIO] [⭐ WATCHLIST]
└─────────────────────────────────────────┘
```

### **Semáforo Logic (Scoring System)**

```
ALGORITMO: Suma ponderada de 6 indicadores

1. TENDENCIA (30%):
   - MA20 > MA50 > MA200: +10pts
   - RSI 40-60: +5pts
   - Precio > Bollinger medio: +5pts

2. MOMENTUM (25%):
   - MACD positivo: +8pts
   - Volumen > promedio: +5pts
   - ROC > 0: +5pts

3. VOLATILIDAD (15%):
   - ATR normal (no extremo): +8pts
   - BB estrechándose: +5pts

4. SOPORTE/RESISTENCIA (15%):
   - Precio > soporte clave: +10pts
   - Distancia a resistencia: +5pts

5. SENTIMIENTO (10%):
   - RSI < 70 (no sobrecomprado): +5pts
   - Stoch K%D no diverge: +5pts

6. VOLUMEN (5%):
   - Vol acumulado creciente: +5pts

SCORING:
🟢 GREEN (BUY):    50-70 puntos
🟡 YELLOW (HOLD):  30-50 puntos
🔴 RED (SELL):     <30 puntos

Confianza = variance + consistency de señales
```

---

## 🛠️ TECHNICAL IMPLEMENTATION

### **Backend: Data Pipeline (Python)**
```python
# analyzer.py
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class TechnicalAnalyzer:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = yf.download(ticker, period="1y")
    
    def calculate_indicators(self):
        """Calcula 15+ indicadores técnicos"""
        df = self.data.copy()
        
        # Moving Averages
        df['MA20'] = df['Close'].rolling(20).mean()
        df['MA50'] = df['Close'].rolling(50).mean()
        df['MA200'] = df['Close'].rolling(200).mean()
        
        # RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # MACD
        exp1 = df['Close'].ewm(span=12).mean()
        exp2 = df['Close'].ewm(span=26).mean()
        df['MACD'] = exp1 - exp2
        df['Signal'] = df['MACD'].ewm(span=9).mean()
        df['MACD_Hist'] = df['MACD'] - df['Signal']
        
        # Bollinger Bands
        df['BB_MA'] = df['Close'].rolling(20).mean()
        df['BB_STD'] = df['Close'].rolling(20).std()
        df['BB_Upper'] = df['BB_MA'] + (df['BB_STD'] * 2)
        df['BB_Lower'] = df['BB_MA'] - (df['BB_STD'] * 2)
        
        # ATR
        df['TR'] = np.maximum(
            df['High'] - df['Low'],
            np.maximum(
                abs(df['High'] - df['Close'].shift()),
                abs(df['Low'] - df['Close'].shift())
            )
        )
        df['ATR'] = df['TR'].rolling(14).mean()
        
        return df
    
    def get_score(self):
        """Retorna score 0-100 para semáforo"""
        df = self.calculate_indicators()
        latest = df.iloc[-1]
        
        score = 0
        
        # Tendencia (30%)
        if latest['MA20'] > latest['MA50'] > latest['MA200']:
            score += 10
        if 40 < latest['RSI'] < 60:
            score += 5
        if latest['Close'] > latest['BB_MA']:
            score += 5
        
        # Momentum (25%)
        if latest['MACD'] > latest['Signal']:
            score += 8
        if latest['Volume'] > df['Volume'].rolling(20).mean().iloc[-1]:
            score += 5
        
        # ... resto de lógica
        
        return {
            'score': score,
            'signal': '🟢 BUY' if score > 50 else ('🟡 HOLD' if score > 30 else '🔴 SELL'),
            'confidence': min(100, score + 20),  # 0-100%
            'indicators': {
                'RSI': round(latest['RSI'], 1),
                'MACD': 'Positivo' if latest['MACD_Hist'] > 0 else 'Negativo',
                'ATR': round(latest['ATR'], 2),
                'Bollinger': 'Dentro' if latest['BB_Lower'] < latest['Close'] < latest['BB_Upper'] else 'Fuera'
            }
        }
```

### **Frontend: React Component Structure**
```
src/
├── components/
│   ├── Dashboard/
│   │   ├── StockGrid.tsx       (tabla principal)
│   │   ├── TrafficLight.tsx    (semáforo 🚦)
│   │   └── QuickFilters.tsx    (filtros)
│   ├── Detail/
│   │   ├── ChartViewer.tsx     (Recharts)
│   │   ├── IndicatorPanel.tsx  (métricas)
│   │   └── Recommendation.tsx  (veredicto)
│   └── Portfolio/
│       ├── PortfolioSummary.tsx
│       └── PositionList.tsx
├── hooks/
│   ├── useStockData.ts         (TanStack Query)
│   └── usePortfolio.ts         (Zustand)
├── utils/
│   ├── scoring.ts              (lógica semáforo)
│   └── formatters.ts
└── pages/
    ├── index.tsx               (dashboard)
    ├── [ticker].tsx            (detail)
    └── portfolio.tsx
```

### **API Endpoints**
```
GET  /api/stocks/list?market=MERVAL|US&limit=50
GET  /api/stocks/:ticker
GET  /api/stocks/:ticker/indicators
GET  /api/stocks/:ticker/chart?period=1m|3m|1y
GET  /api/portfolio
POST /api/portfolio/add
POST /api/portfolio/remove
GET  /api/watchlist
POST /api/watchlist/add
```

---

## 🎨 DESIGN SPECIFICATIONS

### **Color Scheme (Financial Professional)**
```css
--color-primary: #1e40af      /* Azul corporativo */
--color-buy: #10b981          /* Verde esperanza */
--color-hold: #f59e0b         /* Ámbar precaución */
--color-sell: #ef4444         /* Rojo acción */
--bg-dark: #0f172a            /* Casi negro */
--bg-card: #1e293b            /* Gris oscuro */
--text-primary: #f1f5f9       /* Blanco suave */
--accent-chart: #0ea5e9       /* Azul chart */
```

### **Typography**
```
Display:  "Space Mono" (monoespaciado para números)
Body:     "Inter" o "Segoe UI" (legibilidad)
Numbers:  Tabulares + monoespaciado
```

### **Interactions**
- Hover en ticker → highlight + smooth transition
- Click detail → slide panel o modal
- Chart → zoom, brush, tooltip
- Semáforo → pulse animation cuando cambia
- Numbers rojos/verdes → flash transición

---

## 📈 FASES DE DESARROLLO

### **Phase 1 (MVP - 2 semanas)**
- [x] Data pipeline (yfinance)
- [x] Dashboard lista + semáforo básico
- [x] Detail view con charts
- [x] Indicadores técnicos (6 principales)
- [x] Mock portfolio

### **Phase 2 (1-2 semanas)**
- [ ] Autenticación + persistencia real
- [ ] Portfolio manager completo
- [ ] Watchlist personal
- [ ] Alertas por email
- [ ] Histórico de trades

### **Phase 3 (opcional)**
- [ ] Websocket para updates en vivo
- [ ] Screener avanzado (criterios custom)
- [ ] Backtesting de estrategias
- [ ] Community (compartir análisis)

---

## 🚀 STACK DEFINITIVO (RECOMENDADO)

### **Mejor opción (velocidad + escalabilidad)**
```
FRONTEND:
- Next.js 14 (App Router)
- React 18 + TypeScript
- TailwindCSS + shadcn/ui (componentes listos)
- Recharts (charts)
- Zustand (estado)
- TanStack Query (data fetching)

BACKEND:
- FastAPI (Python) para procesamiento financiero
- Express/Node para API REST
- PostgreSQL (Supabase) para persistencia
- Redis (cache)

DEPLOY:
- Vercel (frontend, zero-config)
- Railway o Render (backend)
- GitHub Actions (CI/CD)
```

### **Alternativa ligera (MVP ultra rápido)**
```
FRONTEND:
- Vite + React
- TailwindCSS
- Recharts

BACKEND:
- Python + FastAPI en local
- SQLite
- Deploy en Replit o Vercel Functions
```

---

## 📊 MÉTRICAS CLAVE A MOSTRAR

### Por cada acción:
1. **Precio actual** + cambio %
2. **Semáforo** (🟢🟡🔴) + confianza %
3. **Indicadores técnicos**: RSI, MACD, Bollinger, ATR, EMA
4. **Volumen**: actual vs promedio
5. **Rango 52 semanas**: posición en rango
6. **Fundamentales básicos**: P/E, EPS, Dividend yield
7. **Recomendación**: Texto claro con entrada/salida sugerida

---

## 🔑 VENTAJAS COMPETITIVAS

✅ **Análisis automático**: No requiere expertise técnica  
✅ **Mercados locales**: MERVAL integrado (ventaja AR)  
✅ **Semáforo intuitivo**: Visual inmediato (vs tablas complejas)  
✅ **Mobile-first**: Funciona en cualquier dispositivo  
✅ **Datos frescos**: Actualización cada 5-15 min  
✅ **Sin suscripción**: MVP gratuito (monetizar después)  

---

## ⚠️ CONSIDERACIONES CRÍTICAS

1. **Latencia de datos**: Yahoo Finance tiene 15-20 min de retraso
   - Solución: mostrar hora de última actualización + advertencia

2. **Acciones argentinas**:
   - MERVAL: usar `tickers AAPL.BA`, `GGAL.BA`, etc.
   - Verificar con yfinance qué tickers tiene disponibles
   - Alternativa: integrar API de Invertir Online o SatStock

3. **Disclaimer legal**:
   - "Esto NO es asesoría financiera"
   - "Hacer backtesting antes de usar en real"
   - "Riesgo del usuario al operar"

4. **Performance**:
   - Caché agresivo (5-15 min)
   - Lazy load de charts
   - Virtualización de listas (1000+ tickers)

---

## 🎬 PROMPT PARA GENERAR PRD EJECUTIVO

Si quieres que ChatGPT o Claude generen el PRD detallado, usa esto:

```
Eres un Product Manager de fintech con 10 años en trading platforms.
Crea un PRD EJECUTIVO (máximo 8 páginas) para:

NOMBRE: "TécnicoMX" (o tu nombre)
OBJETIVO: MVP dashboard análisis técnico bursátil

MERCADOS: 
- Argentina (MERVAL: AAPL.BA, GGAL, BBVA, etc.)
- USA (NYSE/NASDAQ: AAPL, MSFT, TSLA, etc.)

FEATURES:
1. Dashboard principal: grid interactivo de acciones
2. Semáforo automático (🟢BUY / 🟡HOLD / 🔴SELL)
3. Detail view: charts + indicadores técnicos
4. Portfolio tracker: posiciones + P&L
5. Watchlist: seguimiento personalizado

INCLUIR:
- User stories (mínimo 5)
- Wireframes (ASCII es OK)
- Criterios de aceptación
- Roadmap 3 fases
- Stack técnico recomendado
- Métricas de éxito

TONO: Ejecutivo, decisivo, accionable.
```

---

## 🎯 PRÓXIMO PASO

**Opción A**: Usa este prompt directamente con Claude Code → genera MVP funcional
**Opción B**: Alimenta a ChatGPT (versión PRD) → obtienes documento formal
**Opción C**: Combina ambos → PRD + prototipo código en paralelo

---

**Creado para**: Tori (SANARTE/TORO)  
**Versión**: 1.0 | MVP-Ready  
**Última actualización**: Marzo 2025  
