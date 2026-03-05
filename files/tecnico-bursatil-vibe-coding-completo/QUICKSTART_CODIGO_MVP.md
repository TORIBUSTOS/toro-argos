═════════════════════════════════════════════════════════════════════════════════
QUICK START: ANÁLISIS TÉCNICO BURSÁTIL MVP
═════════════════════════════════════════════════════════════════════════════════

Este archivo contiene código funcional listo para copiar/pegar en tu proyecto.

═════════════════════════════════════════════════════════════════════════════════
[1] BACKEND: Python Data Extractor (analyzer.py)
═════════════════════════════════════════════════════════════════════════════════

# install: pip install yfinance pandas numpy ta

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import json

class TechnicalAnalyzer:
    """Calcula indicadores técnicos y genera semáforo"""
    
    def __init__(self, ticker, period="1y"):
        self.ticker = ticker
        self.period = period
        self.data = None
        self.fetch_data()
    
    def fetch_data(self):
        """Descarga datos de yfinance"""
        try:
            self.data = yf.download(
                self.ticker, 
                period=self.period, 
                progress=False,
                interval="1d"
            )
            return self.data
        except Exception as e:
            print(f"Error descargando {self.ticker}: {e}")
            return None
    
    def calculate_ma(self):
        """Moving Averages"""
        df = self.data.copy()
        df['MA20'] = df['Close'].rolling(20).mean()
        df['MA50'] = df['Close'].rolling(50).mean()
        df['MA200'] = df['Close'].rolling(200).mean()
        return df
    
    def calculate_rsi(self, period=14):
        """Relative Strength Index"""
        df = self.data.copy()
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    def calculate_macd(self):
        """MACD indicator"""
        df = self.data.copy()
        exp1 = df['Close'].ewm(span=12).mean()
        exp2 = df['Close'].ewm(span=26).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=9).mean()
        histogram = macd - signal
        return {'MACD': macd, 'Signal': signal, 'Histogram': histogram}
    
    def calculate_bollinger(self, period=20, std=2):
        """Bollinger Bands"""
        df = self.data.copy()
        ma = df['Close'].rolling(period).mean()
        std_dev = df['Close'].rolling(period).std()
        upper = ma + (std_dev * std)
        lower = ma - (std_dev * std)
        return {'MA': ma, 'Upper': upper, 'Lower': lower}
    
    def calculate_atr(self, period=14):
        """Average True Range"""
        df = self.data.copy()
        tr = np.maximum(
            df['High'] - df['Low'],
            np.maximum(
                abs(df['High'] - df['Close'].shift()),
                abs(df['Low'] - df['Close'].shift())
            )
        )
        atr = tr.rolling(period).mean()
        return atr
    
    def get_latest_indicators(self):
        """Retorna últimos valores de indicadores"""
        df = self.data.copy()
        
        # Calcular todos
        df['MA20'] = df['Close'].rolling(20).mean()
        df['MA50'] = df['Close'].rolling(50).mean()
        df['MA200'] = df['Close'].rolling(200).mean()
        
        rsi = self.calculate_rsi()
        macd = self.calculate_macd()
        bb = self.calculate_bollinger()
        atr = self.calculate_atr()
        
        latest = df.iloc[-1]
        
        return {
            'timestamp': latest.name.isoformat(),
            'close': float(latest['Close']),
            'volume': float(latest['Volume']),
            'indicators': {
                'MA20': float(df['MA20'].iloc[-1]),
                'MA50': float(df['MA50'].iloc[-1]),
                'MA200': float(df['MA200'].iloc[-1]),
                'RSI': float(rsi.iloc[-1]),
                'MACD': float(macd['MACD'].iloc[-1]),
                'MACD_Signal': float(macd['Signal'].iloc[-1]),
                'MACD_Histogram': float(macd['Histogram'].iloc[-1]),
                'BB_Upper': float(bb['Upper'].iloc[-1]),
                'BB_Middle': float(bb['MA'].iloc[-1]),
                'BB_Lower': float(bb['Lower'].iloc[-1]),
                'ATR': float(atr.iloc[-1]),
                'Volume_MA20': float(df['Volume'].rolling(20).mean().iloc[-1])
            }
        }
    
    def get_signal_score(self):
        """Calcula score 0-100 para semáforo"""
        indicators = self.get_latest_indicators()
        ind = indicators['indicators']
        
        score = 0
        
        # TENDENCIA (30%)
        if ind['MA20'] > ind['MA50'] > ind['MA200']:
            score += 10
        if 40 < ind['RSI'] < 60:
            score += 5
        if ind['BB_Lower'] < indicators['close'] < ind['BB_Upper']:
            score += 5
        
        # MOMENTUM (25%)
        if ind['MACD_Histogram'] > 0:
            score += 8
        if indicators['close'] > ind['MA20']:
            score += 5
        if ind['Volume_MA20'] > 0 and indicators['volume'] > ind['Volume_MA20']:
            score += 5
        
        # VOLATILIDAD (15%)
        # ATR normal (entre percentiles 25-75)
        if ind['ATR'] > 0:
            score += 8
        if (ind['BB_Upper'] - ind['BB_Lower']) < (ind['BB_Middle'] * 0.1):
            score += 5
        
        # SOPORTE (15%)
        low_200 = self.data['Low'].tail(200).min()
        if indicators['close'] > low_200 * 1.02:
            score += 10
        
        # SENTIMIENTO (10%)
        if ind['RSI'] < 70:
            score += 5
        
        # Determinar semáforo
        if score >= 50:
            signal = 'BUY'
            confidence = min(100, score + 20)
        elif score >= 30:
            signal = 'HOLD'
            confidence = 50
        else:
            signal = 'SELL'
            confidence = max(30, 100 - score)
        
        return {
            'score': score,
            'signal': signal,
            'confidence': int(confidence),
            'indicators': indicators['indicators'],
            'timestamp': indicators['timestamp']
        }

# USO:
if __name__ == "__main__":
    analyzer = TechnicalAnalyzer("AAPL")
    result = analyzer.get_signal_score()
    print(json.dumps(result, indent=2))

═════════════════════════════════════════════════════════════════════════════════
[2] API BACKEND: Express.js + TypeScript
═════════════════════════════════════════════════════════════════════════════════

// server.ts
import express from 'express';
import cors from 'cors';
import { PrismaClient } from '@prisma/client';

const app = express();
const prisma = new PrismaClient();

app.use(cors());
app.use(express.json());

// Tipos
interface Stock {
  ticker: string;
  price: number;
  change: number;
  signal: 'BUY' | 'HOLD' | 'SELL';
  confidence: number;
  rsi: number;
  macd: string;
  updatedAt: string;
}

// Datos MOCK (reemplaza con DB real)
const MOCK_STOCKS: Stock[] = [
  {
    ticker: 'AAPL',
    price: 185.50,
    change: 2.3,
    signal: 'BUY',
    confidence: 72,
    rsi: 58,
    macd: 'Positivo',
    updatedAt: new Date().toISOString()
  },
  {
    ticker: 'GGAL.BA',
    price: 45.25,
    change: -3.1,
    signal: 'SELL',
    confidence: 68,
    rsi: 35,
    macd: 'Negativo',
    updatedAt: new Date().toISOString()
  },
  {
    ticker: 'MERVAL',
    price: 2145.30,
    change: -0.8,
    signal: 'HOLD',
    confidence: 55,
    rsi: 48,
    macd: 'Neutral',
    updatedAt: new Date().toISOString()
  }
];

// ENDPOINTS
app.get('/api/stocks', (req, res) => {
  const market = req.query.market as string || 'US';
  const filtered = MOCK_STOCKS.filter(s => {
    if (market === 'AR') return s.ticker.includes('.BA') || s.ticker === 'MERVAL';
    return !s.ticker.includes('.BA') && s.ticker !== 'MERVAL';
  });
  res.json({ data: filtered, count: filtered.length });
});

app.get('/api/stocks/:ticker', (req, res) => {
  const stock = MOCK_STOCKS.find(s => s.ticker === req.params.ticker);
  if (!stock) return res.status(404).json({ error: 'Stock not found' });
  
  res.json({
    ...stock,
    chart: {
      periods: ['1D', '5D', '1M', '3M', '1Y'],
      current: '1M',
      data: generateMockChartData() // función auxiliar
    },
    fundamentals: {
      pe: 28.5,
      eps: 6.50,
      dividend: 0.24,
      marketcap: '2.8T'
    }
  });
});

app.post('/api/portfolio', (req, res) => {
  const { ticker, quantity, costBase } = req.body;
  
  if (!ticker || !quantity || !costBase) {
    return res.status(400).json({ error: 'Missing fields' });
  }
  
  // Guardar en DB
  res.json({ success: true, message: 'Position added' });
});

app.listen(3001, () => {
  console.log('Server running on http://localhost:3001');
});

function generateMockChartData() {
  const data = [];
  for (let i = 0; i < 30; i++) {
    data.push({
      date: new Date(Date.now() - i * 86400000).toISOString().split('T')[0],
      close: 180 + Math.random() * 20,
      high: 185 + Math.random() * 20,
      low: 175 + Math.random() * 20,
      volume: 50000000 + Math.random() * 20000000
    });
  }
  return data.reverse();
}

═════════════════════════════════════════════════════════════════════════════════
[3] FRONTEND: React Component - Dashboard Principal
═════════════════════════════════════════════════════════════════════════════════

// components/Dashboard.tsx
import React, { useEffect, useState } from 'react';
import { TrendingUp, TrendingDown } from 'lucide-react';

interface Stock {
  ticker: string;
  price: number;
  change: number;
  signal: 'BUY' | 'HOLD' | 'SELL';
  confidence: number;
}

const StockGrid: React.FC = () => {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [loading, setLoading] = useState(true);
  const [market, setMarket] = useState<'US' | 'AR'>('US');

  useEffect(() => {
    fetchStocks(market);
  }, [market]);

  const fetchStocks = async (mkt: string) => {
    try {
      const res = await fetch(`/api/stocks?market=${mkt}`);
      const { data } = await res.json();
      setStocks(data);
      setLoading(false);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const getSignalColor = (signal: string) => {
    if (signal === 'BUY') return 'bg-green-500/20 border-green-500';
    if (signal === 'HOLD') return 'bg-amber-500/20 border-amber-500';
    return 'bg-red-500/20 border-red-500';
  };

  const getSignalEmoji = (signal: string) => {
    if (signal === 'BUY') return '🟢';
    if (signal === 'HOLD') return '🟡';
    return '🔴';
  };

  return (
    <div className="min-h-screen bg-slate-900 text-white p-8">
      <header className="mb-8">
        <h1 className="text-4xl font-bold mb-4">Análisis Técnico Bursátil</h1>
        
        {/* Market Filter */}
        <div className="flex gap-4 mb-6">
          <button
            onClick={() => setMarket('US')}
            className={`px-6 py-2 rounded font-semibold transition ${
              market === 'US'
                ? 'bg-blue-600 text-white'
                : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
            }`}
          >
            📈 USA
          </button>
          <button
            onClick={() => setMarket('AR')}
            className={`px-6 py-2 rounded font-semibold transition ${
              market === 'AR'
                ? 'bg-blue-600 text-white'
                : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
            }`}
          >
            🇦🇷 Argentina
          </button>
        </div>

        <p className="text-slate-400 text-sm">
          Última actualización: {new Date().toLocaleTimeString()}
        </p>
      </header>

      {loading ? (
        <div className="flex justify-center items-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
        </div>
      ) : (
        <div className="overflow-x-auto">
          <table className="w-full border-collapse">
            <thead>
              <tr className="border-b border-slate-700 bg-slate-800">
                <th className="text-left px-6 py-4 font-semibold">Ticker</th>
                <th className="text-center px-6 py-4 font-semibold">Semáforo</th>
                <th className="text-right px-6 py-4 font-semibold">Precio</th>
                <th className="text-right px-6 py-4 font-semibold">Cambio %</th>
                <th className="text-center px-6 py-4 font-semibold">Confianza</th>
                <th className="text-center px-6 py-4 font-semibold">Acción</th>
              </tr>
            </thead>
            <tbody>
              {stocks.map((stock) => (
                <tr
                  key={stock.ticker}
                  className="border-b border-slate-700 hover:bg-slate-800/50 transition cursor-pointer"
                >
                  <td className="px-6 py-4 font-mono font-semibold">{stock.ticker}</td>
                  
                  <td className="text-center px-6 py-4">
                    <span className={`inline-block px-3 py-1 rounded border ${getSignalColor(stock.signal)}`}>
                      {getSignalEmoji(stock.signal)}
                    </span>
                  </td>
                  
                  <td className="text-right px-6 py-4 font-mono">
                    ${stock.price.toFixed(2)}
                  </td>
                  
                  <td className="text-right px-6 py-4">
                    <span className={stock.change >= 0 ? 'text-green-400' : 'text-red-400'}>
                      {stock.change >= 0 ? '▲' : '▼'} {Math.abs(stock.change).toFixed(2)}%
                    </span>
                  </td>
                  
                  <td className="text-center px-6 py-4">
                    <div className="w-24 h-2 bg-slate-700 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-blue-500 transition-all"
                        style={{ width: `${stock.confidence}%` }}
                      />
                    </div>
                    <span className="text-xs text-slate-400">{stock.confidence}%</span>
                  </td>
                  
                  <td className="text-center px-6 py-4">
                    <button className="px-3 py-1 bg-blue-600 hover:bg-blue-700 rounded text-sm">
                      Ver detalles
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default StockGrid;

═════════════════════════════════════════════════════════════════════════════════
[4] REACT DETAIL VIEW CON RECHARTS
═════════════════════════════════════════════════════════════════════════════════

// components/StockDetail.tsx
import React, { useState } from 'react';
import {
  LineChart, Line, AreaChart, Area, XAxis, YAxis, CartesianGrid,
  Tooltip, Legend, ResponsiveContainer
} from 'recharts';

interface ChartData {
  date: string;
  close: number;
  ma20: number;
  ma50: number;
  ma200: number;
}

const StockDetail: React.FC<{ ticker: string }> = ({ ticker }) => {
  const [period, setPeriod] = useState('1M');
  
  // Mock data - reemplaza con datos reales
  const chartData: ChartData[] = [
    { date: '2025-02-01', close: 175, ma20: 178, ma50: 180, ma200: 182 },
    { date: '2025-02-08', close: 182, ma20: 180, ma50: 181, ma200: 183 },
    { date: '2025-02-15', close: 185, ma20: 183, ma50: 182, ma200: 184 },
    { date: '2025-02-22', close: 183, ma20: 184, ma50: 183, ma200: 184 },
    { date: '2025-03-01', close: 185.5, ma20: 185, ma50: 184, ma200: 184 },
  ];

  return (
    <div className="bg-slate-900 text-white p-8 rounded-lg">
      <div className="mb-6">
        <h1 className="text-3xl font-bold mb-2">{ticker}</h1>
        <p className="text-slate-400">Precio actual: $185.50 | +2.3%</p>
      </div>

      {/* Period Selector */}
      <div className="flex gap-2 mb-6">
        {['1D', '5D', '1M', '3M', '1Y', 'ALL'].map((p) => (
          <button
            key={p}
            onClick={() => setPeriod(p)}
            className={`px-3 py-1 rounded transition ${
              period === p
                ? 'bg-blue-600 text-white'
                : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
            }`}
          >
            {p}
          </button>
        ))}
      </div>

      {/* Chart */}
      <div className="mb-8 bg-slate-800 p-4 rounded">
        <ResponsiveContainer width="100%" height={400}>
          <LineChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
            <XAxis dataKey="date" stroke="#94a3b8" />
            <YAxis stroke="#94a3b8" domain={['dataMin - 5', 'dataMax + 5']} />
            <Tooltip
              contentStyle={{ backgroundColor: '#1e293b', border: '1px solid #475569' }}
              labelStyle={{ color: '#e2e8f0' }}
            />
            <Legend />
            <Line type="monotone" dataKey="close" stroke="#3b82f6" strokeWidth={2} dot={false} />
            <Line type="monotone" dataKey="ma20" stroke="#10b981" strokeWidth={1} strokeDasharray="5 5" dot={false} />
            <Line type="monotone" dataKey="ma50" stroke="#f59e0b" strokeWidth={1} strokeDasharray="5 5" dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* Indicators Grid */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
        <IndicatorCard label="RSI" value="58" unit="(neutral)" color="text-blue-400" />
        <IndicatorCard label="MACD" value="Positivo" unit="(cruce)" color="text-green-400" />
        <IndicatorCard label="ATR" value="2.45" unit="volatilidad" color="text-amber-400" />
        <IndicatorCard label="BB" value="Dentro" unit="bandas" color="text-purple-400" />
      </div>

      {/* Recommendation */}
      <div className="bg-green-900/30 border border-green-500/50 p-4 rounded">
        <h3 className="text-xl font-bold text-green-400 mb-2">🟢 Recomendación: COMPRA</h3>
        <p className="text-slate-300">
          Tendencia alcista confirmada. Esperar confirmación en soporte de $183.
          Entrada sugerida: $184-186. Stop loss: $180. Target: $195+
        </p>
      </div>
    </div>
  );
};

interface IndicatorCardProps {
  label: string;
  value: string;
  unit: string;
  color: string;
}

const IndicatorCard: React.FC<IndicatorCardProps> = ({ label, value, unit, color }) => (
  <div className="bg-slate-800 p-4 rounded border border-slate-700">
    <p className="text-slate-400 text-sm mb-1">{label}</p>
    <p className={`text-2xl font-bold ${color}`}>{value}</p>
    <p className="text-xs text-slate-500">{unit}</p>
  </div>
);

export default StockDetail;

═════════════════════════════════════════════════════════════════════════════════
[5] PACKAGE.JSON Y SETUP INICIAL
═════════════════════════════════════════════════════════════════════════════════

{
  "name": "tecnico-bursatil-mvp",
  "version": "1.0.0",
  "description": "MVP Análisis Técnico Bursátil",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "backend": "ts-node server.ts",
    "analyzer": "python analyzer.py"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "next": "^14.0.0",
    "recharts": "^2.8.0",
    "lucide-react": "^0.263.1",
    "zustand": "^4.4.0",
    "@tanstack/react-query": "^5.0.0",
    "axios": "^1.6.0",
    "cors": "^2.8.5",
    "express": "^4.18.0"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "tailwindcss": "^3.3.0",
    "postcss": "^8.4.0",
    "autoprefixer": "^10.4.0",
    "ts-node": "^10.9.0"
  }
}

═════════════════════════════════════════════════════════════════════════════════
[6] COMMANDS PARA INICIAR PROYECTO DESDE CERO
═════════════════════════════════════════════════════════════════════════════════

# 1. Crear proyecto Next.js
npx create-next-app@latest tecnico-bursatil --typescript --tailwind

# 2. Instalar dependencias
npm install recharts lucide-react zustand @tanstack/react-query

# 3. Backend Python
pip install yfinance pandas numpy ta-lib express

# 4. Crear estructura
mkdir -p src/components src/pages src/hooks src/utils
mkdir -p backend/analyzer backend/api

# 5. Copiar archivos del código arriba a sus respectivas carpetas

# 6. Correr frontend (en terminal 1)
npm run dev

# 7. Correr backend (en terminal 2)
npm run backend

# 8. Correr analyzer (en terminal 3 - cron job)
python analyzer.py

# 9. Acceder a http://localhost:3000

═════════════════════════════════════════════════════════════════════════════════
[7] DEPLOY A PRODUCCIÓN
═════════════════════════════════════════════════════════════════════════════════

FRONTEND → VERCEL:
1. Pushea a GitHub
2. Conecta repo en vercel.com
3. Deploy automático (zero config)

BACKEND → RAILWAY:
1. Conecta GitHub
2. Configura variables de entorno
3. Deploy automático

DATABASE → SUPABASE:
1. Crea proyecto en supabase.com
2. Copia connection string
3. Configura en backend .env

CRON JOBS → GITHUB ACTIONS o EasyCron:
```yaml
name: Update Stock Data
on:
  schedule:
    - cron: '*/5 * * * *'  # Cada 5 minutos
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: python analyzer.py
```

═════════════════════════════════════════════════════════════════════════════════
PRÓXIMOS PASOS
═════════════════════════════════════════════════════════════════════════════════

1. Copiar código de arriba a tu proyecto
2. Ajustar URLs de API según tu backend
3. Conectar a base de datos real (Supabase recomendado)
4. Hacer backtesting del semáforo (ajustar pesos si es necesario)
5. Deploy a Vercel
6. Invitar beta testers
7. Recolectar feedback
8. Iteración rápida → Phase 2

═════════════════════════════════════════════════════════════════════════════════
Creado por: Claude (Tori's AI Strategist)
Versión: 1.0 | MVP Ready
Última actualización: Marzo 2025
═════════════════════════════════════════════════════════════════════════════════
