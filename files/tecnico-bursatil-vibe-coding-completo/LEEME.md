═════════════════════════════════════════════════════════════════════════════════
📖 LÉEME - EXPLICACIÓN DEL PROYECTO EN LENGUAJE NATURAL
═════════════════════════════════════════════════════════════════════════════════

Si no eres developer, este es tu documento.
Explicamos QUÉ ES, CÓMO FUNCIONA y POR QUÉ ESTÁ HECHO ASÍ.
Sin código, sin jerga técnica (o explicada cuando necesaria).

═════════════════════════════════════════════════════════════════════════════════
🎯 LA IDEA EN 1 MINUTO
═════════════════════════════════════════════════════════════════════════════════

Imagina que tienes un "experto en bolsa" que:
✅ Mira el precio de 1000 acciones
✅ Analiza 10 indicadores técnicos para cada una
✅ Te dice "COMPRA esta" 🟢, "VENDE esa" 🔴, "MANTÉN la otra" 🟡
✅ Todo en 2 segundos
✅ Sin cansarse
✅ 24/7

ESE es el proyecto: Un software que hace exactamente eso.
Para acciones de Argentina + Estados Unidos.

═════════════════════════════════════════════════════════════════════════════════
📊 QUÉ ES (EXPLICADO SIMPLE)
═════════════════════════════════════════════════════════════════════════════════

NOMBRE: "Análisis Técnico Bursátil" (o "Técnico Bursátil MVP")

PROPÓSITO: Ayudar traders/inversionistas a tomar decisiones rápidas
           Mostrando qué hacer (comprar/vender/mantener) basado en matemática

MERCADOS: Argentina (MERVAL) + Estados Unidos (NYSE, NASDAQ)

USUARIOS: 
  • Traders activos (quieren decisiones rápido)
  • Inversionistas retail (quieren entender qué pasa)
  • Principiantes (quieren aprender a invertir)

PROBLEMA QUE RESUELVE:
  ❌ TradingView es complejo, requiere expertise
  ❌ Bloomberg es caro ($$$)
  ❌ Decisión manual toma tiempo
  ✅ Este software: Simple, rápido, automático

═════════════════════════════════════════════════════════════════════════════════
⚙️ CÓMO FUNCIONA (ANALOGÍA SIMPLE)
═════════════════════════════════════════════════════════════════════════════════

IMAGINA UN SISTEMA DE SEMÁFORO PARA INVERSIONES:

🟢 VERDE (COMPRA):
   "Todas las señales son positivas. Comprar ahora es buena idea"
   Qué significa: Tendencia alcista + momentum positivo + RSI neutral
   Confianza: 72% (no es 100%, pero es seguro)

🟡 AMARILLO (MANTENER):
   "Está confuso. Espera a más información"
   Qué significa: Señales mixtas, ni claramente alcista ni bajista
   Confianza: 55% (muy indeciso)

🔴 ROJO (VENTA):
   "Las señales dicen que venda ahora"
   Qué significa: Tendencia bajista + momentum negativo
   Confianza: 68% (bastante seguro de que es venta)

CÓMO FUNCIONA INTERNAMENTE:
┌─────────────────────────────────────────────────────┐
│ 1. TRAE DATOS                                       │
│    • Baja precio de acciones de yfinance (API)      │
│    • Cada 5 minutos automáticamente                 │
│                                                     │
│ 2. CALCULA INDICADORES                              │
│    • RSI (¿está sobrecomprado/sobrevendido?)        │
│    • MACD (¿hay cambio de tendencia?)               │
│    • Bollinger Bands (¿dónde está el precio?)       │
│    • ATR (¿qué tan volátil es?)                     │
│    • Y más...                                        │
│                                                     │
│ 3. GENERA SCORE                                      │
│    • Suma todos los indicadores                     │
│    • Pondera cada uno (tendencia vale más que ruido)│
│    • Resultado: número 0-100                        │
│                                                     │
│ 4. DECIDE SEMÁFORO                                  │
│    • Score 50-70 → 🟢 COMPRA                        │
│    • Score 30-50 → 🟡 MANTÉN                        │
│    • Score <30 → 🔴 VENDE                           │
│                                                     │
│ 5. MUESTRA EN PANTALLA                              │
│    • Tabla bonita con colores                       │
│    • Puedes clickear para ver análisis detallado    │
└─────────────────────────────────────────────────────┘

═════════════════════════════════════════════════════════════════════════════════
🖥️ QUÉ VES EN PANTALLA
═════════════════════════════════════════════════════════════════════════════════

PANTALLA 1: DASHBOARD (Inicio)
───────────────────────────────

┌────────────────────────────────────────────────────┐
│ ANÁLISIS TÉCNICO BURSÁTIL                          │
│ [Mercado: USA] [Mercado: Argentina]                │
├────────────────────────────────────────────────────┤
│ TICKER │ 🟢 SEMÁFORO │ PRECIO  │ CAMBIO  │ CONF    │
├────────────────────────────────────────────────────┤
│ AAPL   │    🟢       │ $185.50 │ +2.3%  │ 72%     │
│ GGAL   │    🔴       │ $45.25  │ -3.1%  │ 68%     │
│ MERVAL │    🟡       │ 2145.30 │ -0.8%  │ 55%     │
│ MSFT   │    🟢       │ $412.30 │ +1.8%  │ 78%     │
└────────────────────────────────────────────────────┘

QUÉ SIGNIFICA CADA COLUMNA:
  • TICKER: Nombre de la acción (AAPL = Apple)
  • SEMÁFORO: 🟢 compra, 🟡 mantén, 🔴 vende
  • PRECIO: Precio actual de la acción
  • CAMBIO: Subió/bajó cuánto en % hoy
  • CONF: Confianza del análisis (0-100%)

ACCIÓN: Click en una fila → abre análisis detallado


PANTALLA 2: ANÁLISIS DETALLADO
───────────────────────────────

┌────────────────────────────────────────────────────┐
│ APPLE (AAPL)                                       │
│ Precio: $185.50 | Cambio: +2.3%                   │
│                                                    │
│ 🟢 SEMÁFORO: COMPRA (Confianza: 72%)               │
│                                                    │
│ [GRÁFICO de precio últimas 4 semanas]              │
│ [Con líneas de tendencia y bandas]                 │
│                                                    │
│ INDICADORES:                                       │
│  • RSI: 58 (neutral - buen punto de entrada)      │
│  • MACD: Positivo (tendencia alcista)              │
│  • ATR: 2.45 (volatilidad normal)                  │
│  • Bollinger: Dentro de bandas (normal)            │
│                                                    │
│ RECOMENDACIÓN:                                     │
│ "Compra entre $183-186. Stop loss: $180.           │
│  Objetivo: $195+. Tendencia alcista fuerte."       │
│                                                    │
│ [+ Agregar a mi portafolio]                       │
│ [⭐ Guardar en watchlist]                           │
└────────────────────────────────────────────────────┘

QUÉ VES:
  • Gráfico histórico (cómo subió/bajó en últimas semanas)
  • Todos los indicadores técnicos en números
  • Recomendación clara (dónde entrar, dónde salir, dónde perder)
  • Botones para seguir esta acción o agregarla a tu portafolio


PANTALLA 3: MI PORTAFOLIO
──────────────────────────

┌────────────────────────────────────────────────────┐
│ 📊 MI PORTAFOLIO                                   │
│ Valor Total: $52,300 | Ganancia: +$17,300 (+49%)  │
│                                                    │
│ ┌────────────────────────────────────────────┐   │
│ │ AAPL - 100 acciones                        │   │
│ │ Compré a $150 c/u → Ahora $185.50 c/u     │   │
│ │ Invertido: $15,000 → Ahora: $18,550       │   │
│ │ GANANCIA: +$3,550 (+23.7%) 🟢             │   │
│ │ Es 35% de mi portafolio                    │   │
│ │ [Editar cantidad] [Vender]                 │   │
│ └────────────────────────────────────────────┘   │
│                                                    │
│ ┌────────────────────────────────────────────┐   │
│ │ BTC-USD (Bitcoin) - 0.5 BTC                │   │
│ │ Compré a $40,000 c/u → Ahora $67,500      │   │
│ │ Invertido: $20,000 → Ahora: $33,750       │   │
│ │ GANANCIA: +$13,750 (+68.75%) 🟢🟢         │   │
│ │ Es 65% de mi portafolio                    │   │
│ │ [Editar cantidad] [Vender]                 │   │
│ └────────────────────────────────────────────┘   │
│                                                    │
│ [+ Agregar nueva posición]                        │
└────────────────────────────────────────────────────┘

QUÉ VES:
  • Resumen total de tu inversión
  • Cada posición (acción/crypto que tienes)
  • Cuánto pagaste vs. cuánto vale ahora
  • Ganancia/pérdida en dinero y porcentaje
  • Qué % de tu portafolio es cada uno

═════════════════════════════════════════════════════════════════════════════════
💡 CONCEPTOS CLAVE (EXPLICADOS SIMPLE)
═════════════════════════════════════════════════════════════════════════════════

ANÁLISIS TÉCNICO
────────────────
Qué es: Mirar gráficos históricos de precios + patrones para adivinar qué pasa después
Por qué funciona: Los precios no cambian al azar, hay patrones
Este software: Automatiza ese análisis (en lugar de que lo hagas vos)

INDICADORES TÉCNICOS
────────────────────
Qué son: Fórmulas matemáticas que procesan precios históricos

RSI (Relative Strength Index):
  • Mide si la acción está "sobrecomprada" (sube demasiado) o "sobrevendida" (baja demasiado)
  • 0-30: Sobrevendida (probablemente suba)
  • 70-100: Sobrecomprada (probablemente baje)
  • 40-60: Neutral (puede ir para cualquier lado)

MACD (Moving Average Convergence Divergence):
  • Mira tendencias a largo vs corto plazo
  • Si la línea rápida cruza la lenta HACIA ARRIBA: tendencia alcista 🟢
  • Si cruza hacia ABAJO: tendencia bajista 🔴

Bollinger Bands:
  • Dibuja 3 líneas alrededor del precio
  • Línea del medio: promedio de precios
  • Líneas de arriba/abajo: límites de volatilidad normal
  • Si el precio toca el límite = extremo, probablemente vuelva al medio

ATR (Average True Range):
  • Mide volatilidad (qué tan "loco" sube/baja)
  • ATR alto: acción volátil, puede perder dinero rápido
  • ATR bajo: acción estable, menos riesgo

SEMÁFORO (El score final)
─────────────────────────
El software suma todos los indicadores:
  • 30% por tendencia (hacia dónde va)
  • 25% por momentum (qué tan fuerte sube/baja)
  • 15% por volatilidad (qué tan loco se mueve)
  • 15% por soporte (hay piso o puede caer más)
  • 10% por sentimiento (no está extremo)
  • 5% por volumen (hay mucha gente comprando/vendiendo)

Resultado: Un número 0-100 que se convierte en:
  🟢 Compra (50-70): Señales positivas dominan
  🟡 Mantén (30-50): Muy dividido, espera claridad
  🔴 Vende (<30): Señales negativas dominan

═════════════════════════════════════════════════════════════════════════════════
🏗️ CÓMO ESTÁ CONSTRUIDO (ARQUITECTURA SIMPLE)
═════════════════════════════════════════════════════════════════════════════════

PARTE 1: EL CEREBRO (Backend)
─────────────────────────────
"El cerebro" hace todo el cálculo:
  ✓ Baja datos de precios (de yfinance)
  ✓ Calcula indicadores (fórmulas matemáticas)
  ✓ Genera score del semáforo
  ✓ Guarda todo en base de datos
  ✓ Cada 5 minutos se actualiza automáticamente

Dónde corre: En un servidor en la nube (Railway)
Cuándo: 24/7 (sin parar)
Lenguaje: Python (porque es bueno para matemática)

PARTE 2: LOS OJOS (Frontend)
────────────────────────────
"Los ojos" es lo que ves en pantalla:
  ✓ La tabla bonita de acciones
  ✓ Los gráficos
  ✓ Los botones de clickear
  ✓ Tu portafolio personal
  ✓ La watchlist de favoritos

Dónde corre: Tu navegador
Cuándo: Cuando tú lo abres
Lenguaje: JavaScript + React (para hacer cosas bonitas)

PARTE 3: EL MEDIO (API)
───────────────────────
"El medio" es cómo el cerebro habla con los ojos:
  • Frontend pregunta: "¿Cuál es el análisis de AAPL?"
  • Backend responde: "Aquí están los datos: precio X, RSI Y, semáforo Z"
  • Frontend muestra en pantalla: Tabla + Gráficos + Números

Protocolo: REST (simplemente: preguntas y respuestas en JSON)

PARTE 4: LA MEMORIA (Base de datos)
────────────────────────────────────
"La memoria" guarda información:
  ✓ Precios históricos
  ✓ Indicadores calculados
  ✓ Tu portafolio
  ✓ Tu watchlist

Dónde: PostgreSQL (base de datos en la nube - Supabase)
Cuándo: Siempre (datos persisten)

DIAGRAMA SIMPLE:
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  TÚ EN NAVEGADOR                                        │
│  ↓                                                      │
│  [Tabla bonita] ← Frontend (React) ← API REST          │
│  [Gráficos]                           ↑                 │
│  [Botones]    ← JavaScript/TailwindCSS│                 │
│                                        │                 │
│                                    Backend (Python)     │
│                                    • Descarga datos     │
│                                    • Calcula indicadores│
│                                    • Genera semáforo    │
│                                    • Guarda en DB       │
│                                        ↓                 │
│                                    PostgreSQL           │
│                                    (Base de datos)      │
│                                                         │
└─────────────────────────────────────────────────────────┘

═════════════════════════════════════════════════════════════════════════════════
🚀 CÓMO SE DESARROLLA (VIBE CODING EXPLICADO)
═════════════════════════════════════════════════════════════════════════════════

Tori (emprendedor) NO ESCRIBE CÓDIGO.
En su lugar, usa agentes IA que SÍ escriben código.

FLUJO NORMAL (developer humano):
Tori: "Necesito componente X" → Espera 2 días → Developer lo hace

FLUJO VIBE CODING (con agentes IA):
Tori: "Necesito componente X" → Escribe en ChatGPT → Claude Code lo hace en 5 min

CÓMO FUNCIONA:

1. TÚ (TORI) ESCRIBE QUÉ NECESITAS EN CHATGPT
   "Quiero un componente que muestre tabla de stocks con:
    - Ticker, precio, semáforo, cambio %
    - Clickeable para abrir detalles
    - Responsive en mobile
    - Colores oscuros profesionales"

2. CHATGPT DEVUELVE "BLOQUE NEGRO" (CÓDIGO LISTO)
   Un cuadro gris con código JavaScript/Python que funciona.
   No es teoría, es código real que puedes copiar/pegar.

3. TÚ COPIAS ESE CÓDIGO

4. TÚ LO PASAS A CLAUDE CODE (AGENTE IA)
   "Integra este componente en el proyecto"

5. CLAUDE CODE AUTOMÁTICAMENTE:
   ✓ Lo pone en la carpeta correcta
   ✓ Conecta con otros archivos
   ✓ Verifica que no haya errores
   ✓ Lo prueba
   ✓ Te dice "Listo ✅"

6. RESULTADO:
   El componente está en tu proyecto, funcionando.
   Sin que hayas escribido ni una línea de código.

AGENTES IA DISPONIBLES:

Claude Code:
  • Escribe código frontend (lo que ves en pantalla)
  • Crea componentes React
  • Diseña interfaces bonitas
  • Usa TailwindCSS + shadcn/ui para estilo

Antigravity:
  • Escribe código backend (el cerebro)
  • Crea APIs (cómo habla frontend con base de datos)
  • Configura bases de datos
  • Despliega a producción

VENTAJA:
  • Desarrollo 10x más rápido
  • Sin tener que aprender a programar
  • Costo bajo (pagas el API, no developers)
  • Control total (vos decides qué hacer)

═════════════════════════════════════════════════════════════════════════════════
📅 TIMELINE: CÓMO AVANZA EL PROYECTO
═════════════════════════════════════════════════════════════════════════════════

NO es "Semana 1, 2, 3" (timeline rígido).
Es "Proceso 1, Proceso 2, Proceso 3" (etapas lógicas).

PROCESO 1: BACKEND (El cerebro)
───────────────────────────────
Qué pasa:
  • Creas TechnicalAnalyzer (descarga datos + calcula indicadores)
  • Creas Scoring (genera el semáforo)
  • Creas API (cómo pide datos el frontend)
  • Creas Base de datos (guarda información)

Quién: Antigravity (agente backend)
Duración: 2-3 días
Resultado: Puedes preguntar "¿Cuál es el análisis de AAPL?" y recibes respuesta JSON

Test: Llamas /api/stocks/AAPL en navegador y devuelve datos


PROCESO 2: FRONTEND (Los ojos)
──────────────────────────────
Qué pasa:
  • Creas Dashboard (tabla bonita de acciones)
  • Creas Detail View (gráficos + indicadores)
  • Creas Portfolio (mi portafolio personal)
  • Creas Watchlist (acciones favoritas)

Quién: Claude Code (agente frontend)
Duración: 2-3 días
Resultado: Abres navegador y ves tabla bonita, clickeable, funcional

Test: npm run dev → http://localhost:3000 → ves dashboard funcionando


PROCESO 3: DEPLOY (Poner en vivo)
──────────────────────────────────
Qué pasa:
  • Configuras autenticación (login/password)
  • Empaquetas todo en Docker (contenedores)
  • Subes frontend a Vercel (servidor web)
  • Subes backend a Railway (servidor Python)
  • Configuras base de datos en Supabase
  • Configuras CI/CD (auto-deploy cuando haces cambios)

Quién: Antigravity (agente infra)
Duración: 1-2 días
Resultado: Tu app está VIVA en internet. Puedes compartir URL y otros usuarios usan

Test: Abres https://tuapp.vercel.app → ves dashboard en vivo


TOTAL: 5-8 DÍAS PARA MVP COMPLETO
(Con agentes IA haciendo el trabajo)

═════════════════════════════════════════════════════════════════════════════════
💰 POR QUÉ ESTA FORMA ES RENTABLE
═════════════════════════════════════════════════════════════════════════════════

FORMA TRADICIONAL:
  • Contratar 1-2 developers: $3,000-5,000/mes
  • Esperar 4-8 semanas para MVP
  • Riesgo: Si proyecto falla, perdiste $15-40k

FORMA VIBE CODING (Este proyecto):
  • Cero desarrolladores contratados
  • MVP en 1 semana ($100 en APIs)
  • Si falla: Perdiste $100, no $40k
  • Si funciona: Escalas sin overhed de developers

AHORRO: 85-95% en costo
VELOCIDAD: 4-8x más rápido

═════════════════════════════════════════════════════════════════════════════════
❓ PREGUNTAS FRECUENTES (FAQ)
═════════════════════════════════════════════════════════════════════════════════

P: ¿Es legal hacer análisis técnico automático?
R: SÍ. No estás haciendo asesoría financiera (eso sería ilegal).
   Estás dando "análisis técnico" que el usuario interpreta.
   (Disclaimer: "No es asesoría financiera, solo análisis")

P: ¿Qué pasa si los datos de yfinance son incorrectos?
R: yfinance tiene 15-20 min de retraso (datos viejos). Es normal.
   Para trading activo (segundos), necesitarías datos en vivo (caro).
   Para inversión (days/weeks), 15 min no importa.

P: ¿Funciona en el teléfono?
R: SÍ. Frontend está diseñado responsive (se adapta).
   Abres en navegador mobile y funciona igual.

P: ¿Cuándo se actualiza el análisis?
R: Cada 5 minutos automáticamente (cron job en backend).
   Tú solo abres y ves datos frescos.

P: ¿Puedo usarlo para trading automático (ejecutar órdenes)?
R: No, por ahora. Es solo análisis.
   Tú lees el análisis → TÚ decides si comprar/vender.
   (Agregar trading automático = Fase 2)

P: ¿Qué pasa si quiero agregar más funcionalidades?
R: Mismo proceso. Escribís en ChatGPT → Bloque negro → Claude Code/Antigravity.
   Escalable sin límite.

P: ¿Dónde está mi información guardada?
R: En Supabase PostgreSQL (en la nube, seguro, encriptado).
   No la vendemos, no la compartimos (privacy by default).

P: ¿Cuánto cuesta esto?
R: MVP: ~$0 (franja gratuita de Vercel + Supabase)
   Si crece:
     • Vercel: $20/mes
     • Supabase: $25/mes
     • Railway: $5-20/mes
     • Total: ~$50-100/mes para miles de usuarios

P: ¿Qué pasa si hay un crash/error?
R: Tenemos monitoreo (Vercel Analytics + logs en Railway).
   Si algo explota, ves el error y avisas al agente.
   Agente arrregla en minutos.

═════════════════════════════════════════════════════════════════════════════════
🎯 TU PRÓXIMO PASO
═════════════════════════════════════════════════════════════════════════════════

1. Lee este documento completo (LÉEME.md) ✅
2. Abre ÍNDICE_GENERAL.md (guía de navegación)
3. Lee VIBE_CODING_WORKFLOW.md (cómo trabajan los agentes)
4. Completa FORMULARIO_CODESENO_UX_UI.md (elige tus colores/estilos)
5. Devuélveme el formulario respondido
6. Yo hago mockups basados en tus decisiones
7. Agentes IA comienzan a codificar

═════════════════════════════════════════════════════════════════════════════════

**RESUMEN: Este es un software que analiza miles de acciones automáticamente y te dice si comprar/vender/mantener. Está hecho sin escribir código tradicional, usando agentes IA que hacen el trabajo en horas en lugar de semanas. Es rápido, barato y escalable.**

═════════════════════════════════════════════════════════════════════════════════
Versión: 1.0
Fecha: Marzo 2025
Para: Tori @ TORO Holdings (y cualquiera que no sea developer)
═════════════════════════════════════════════════════════════════════════════════
