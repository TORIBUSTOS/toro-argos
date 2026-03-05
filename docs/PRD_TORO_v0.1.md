# PRD TORO v0.1

**Producto:** MVP 6 (nombre pendiente)\
**Sistema:** TORO\
**Autores:** Tori + Rosario\
**Estado:** Draft operativo

------------------------------------------------------------------------

## 1. Visión del producto

TORO es una plataforma que permite **analizar acciones y detectar
oportunidades de mercado de forma rápida y estructurada**, utilizando
análisis técnico automatizado y una interfaz diseñada para la toma de
decisiones.

El sistema transforma el análisis manual disperso en **un radar
operativo claro** donde el usuario puede:

-   detectar oportunidades
-   evaluar activos rápidamente
-   monitorear su cartera
-   interpretar indicadores técnicos sin fricción

------------------------------------------------------------------------

## 2. Problema que resuelve

Los inversores particulares suelen usar múltiples herramientas
desconectadas:

-   TradingView → gráficos
-   Investing → datos
-   planillas personales → seguimiento de cartera
-   análisis manual → interpretación

Esto genera:

-   análisis lento
-   dificultad para comparar activos
-   señales poco claras
-   decisiones poco estructuradas

TORO centraliza estas tareas en **un sistema único de análisis
operativo**.

------------------------------------------------------------------------

## 3. Usuario objetivo

### Usuario primario

Inversor particular que utiliza análisis técnico.

Perfil típico:

-   revisa el mercado regularmente
-   utiliza TradingView / Investing
-   analiza indicadores técnicos
-   mantiene cartera propia

### Usuario secundario

Trader o analista que busca **un radar rápido de oportunidades**.

------------------------------------------------------------------------

## 4. Propuesta de valor

TORO ofrece cinco capacidades principales.

### 4.1 Radar de mercado

Lista de activos analizados automáticamente.

Muestra:

-   precio
-   cambio %
-   score técnico
-   señal de trading

### 4.2 Señal técnica clara

Cada activo recibe una señal:

🟢 BUY\
🟡 HOLD\
🔴 SELL

### 4.3 Análisis técnico automático

Indicadores calculados:

-   RSI
-   MACD
-   Bollinger Bands
-   ATR
-   medias móviles
-   volumen

### 4.4 Watchlist

Permite guardar activos para monitoreo.

### 4.5 Seguimiento de cartera

Permite registrar posiciones y ver:

-   P&L
-   peso de cada activo
-   evolución general

------------------------------------------------------------------------

## 5. Alcance del MVP v0.1

El MVP se enfoca en tres capacidades centrales.

### 5.1 Dashboard de mercado

Tabla principal con:

-   ticker
-   precio
-   cambio %
-   señal
-   score técnico
-   volumen

Funciones:

-   filtro por mercado
-   búsqueda por ticker

### 5.2 Vista detallada por activo

Ruta:

/stocks/{ticker}

Incluye:

-   gráfico de precio
-   indicadores técnicos
-   score del activo
-   interpretación técnica

### 5.3 Watchlist

Guardar activos y monitorear señales.

### 5.4 Portfolio tracker

Registrar posiciones y analizar:

-   P&L
-   distribución

### 5.5 Motor de análisis técnico

Backend que:

-   descarga datos de mercado
-   calcula indicadores
-   genera score
-   produce señal de trading

------------------------------------------------------------------------

## 6. Arquitectura del sistema

### Backend

Tecnología:

Python + FastAPI

Componentes:

-   TechnicalAnalyzer
-   ScoringEngine
-   API REST

Base de datos:

PostgreSQL

### Frontend

Tecnología:

React / Next.js

Componentes:

-   Dashboard
-   DetailView
-   Watchlist
-   Portfolio

UI:

TailwindCSS + shadcn/ui

------------------------------------------------------------------------

## 7. Modelo de interfaz

Proceso:

1.  Rosario genera prototipo HTML
2.  Tori evalúa el layout
3.  Ajustes
4.  Aprobación
5.  Implementación en React

------------------------------------------------------------------------

## 8. Protocolo de desarrollo TORO

Roles:

**Tori --- Orquestador**\
Define dirección y decisiones.

**Rosario --- Arquitecta**\
Diseña sistema y genera bloques de código.

**Agentes IA --- Operativos**

Claude Code → frontend\
Antigravity → backend / infraestructura

Flujo:

Tori → Rosario → bloque negro → agente → integración

------------------------------------------------------------------------

## 9. Roadmap inicial

**Fase 1**\
Motor de análisis técnico

**Fase 2**\
Dashboard + vista detallada

**Fase 3**\
Watchlist + portfolio

**Fase 4**\
Infraestructura y deploy

------------------------------------------------------------------------

## 10. Principios del sistema

-   UI definida antes del código
-   bloques negros como unidad de ejecución
-   agentes ejecutan, humanos deciden
-   MVP primero, expansión después

------------------------------------------------------------------------

**Estado:** PRD TORO v0.1 --- Draft completo
