# PRD TORO v0.2

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

### Radar de mercado

Lista de activos analizados automáticamente.

Muestra:

-   precio
-   cambio %
-   score técnico
-   señal de trading

### Señal técnica clara

Cada activo recibe una señal:

🟢 BUY\
🟡 HOLD\
🔴 SELL

### Análisis técnico automático

Indicadores calculados:

-   RSI
-   MACD
-   Bollinger Bands
-   ATR
-   medias móviles
-   volumen

### Watchlist

Permite guardar activos para monitoreo.

### Seguimiento de cartera

Permite registrar posiciones y ver:

-   P&L
-   peso de cada activo
-   evolución general

------------------------------------------------------------------------

## 5. Alcance del MVP

### Dashboard de mercado

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

### Vista detallada por activo

Ruta:

/stocks/{ticker}

Incluye:

-   gráfico de precio
-   indicadores técnicos
-   score del activo
-   interpretación técnica

### Watchlist

Guardar activos y monitorear señales.

### Portfolio tracker

Registrar posiciones y analizar:

-   P&L
-   distribución

### Motor de análisis técnico

Backend que:

-   descarga datos de mercado
-   calcula indicadores
-   genera score
-   produce señal de trading

------------------------------------------------------------------------

## 6. Universo de activos

### Acciones subyacentes de CEDEARs

El sistema analiza las acciones originales de los CEDEARs listados en
BYMA.

El análisis se realiza sobre el activo original en su mercado primario
(NYSE / NASDAQ) para evitar distorsiones por tipo de cambio o spreads.

### Filtro de liquidez

No todos los CEDEARs serán incluidos.

Criterio inicial sugerido:

-   volumen promedio 30 días \> 500.000 USD

Resultado esperado:

200 CEDEARs aproximados → filtrado a \~100 activos líquidos.

### Mercado argentino (BYMA)

El radar incluye:

Panel Líder (MERVAL)\
Panel General

También puede aplicarse filtro de liquidez.

### Universo final estimado

120 -- 180 activos analizados.

------------------------------------------------------------------------

## 7. Modelo de señal técnica

Sistema tipo **semáforo**.

Estados:

SELL\
HOLD\
BUY

Visualización tipo gauge:

ROJO → AMARILLO → VERDE

------------------------------------------------------------------------

## 8. Modelo de scoring técnico

Cada activo tiene un **score técnico de 0 a 100**.

  Score     Señal
  --------- -------
  0--30     SELL
  30--60    HOLD
  60--100   BUY

Indicadores iniciales:

-   RSI
-   MACD
-   Media móvil 50
-   Media móvil 200
-   Volumen
-   Momentum

------------------------------------------------------------------------

## 9. Flujo de datos

Datos de mercado\
↓\
Descarga de precios históricos\
↓\
Cálculo de indicadores técnicos\
↓\
Motor de scoring\
↓\
Generación de señal\
↓\
API TORO\
↓\
Dashboard

------------------------------------------------------------------------

## 10. Datos almacenados

ticker\
mercado\
precio_actual\
cambio_diario\
volumen

RSI\
MACD\
media_50\
media_200\
ATR

score_tecnico\
señal\
timestamp

------------------------------------------------------------------------

## 11. Frecuencia de actualización

Inicial:

actualización diaria

Futuro:

actualización intradía

------------------------------------------------------------------------

## 12. APIs de mercado

Posibles fuentes:

-   Finnhub
-   Alpha Vantage
-   Polygon
-   Yahoo Finance

Finnhub se utilizará inicialmente.

------------------------------------------------------------------------

## 13. Arquitectura técnica

### Backend

Python + FastAPI

Componentes:

-   TechnicalAnalyzer
-   ScoringEngine
-   MarketDataFetcher
-   API REST

Base de datos:

PostgreSQL

### Frontend

React / Next.js

Componentes:

-   Dashboard
-   Asset Detail View
-   Watchlist
-   Portfolio

UI:

TailwindCSS + shadcn/ui

------------------------------------------------------------------------

## 14. Modelo de interfaz

Proceso:

1.  Rosario crea prototipo HTML
2.  Tori revisa layout
3.  ajustes
4.  aprobación
5.  implementación en React

------------------------------------------------------------------------

## 15. Roadmap

Fase 1 --- motor técnico\
Fase 2 --- dashboard mercado\
Fase 3 --- vista por activo\
Fase 4 --- watchlist\
Fase 5 --- portfolio\
Fase 6 --- deploy

------------------------------------------------------------------------

## 16. Protocolo de desarrollo TORO

Metodología: **Vibe Coding**

Roles:

Tori --- Orquestador\
Rosario --- Arquitecta

Agentes IA:

Claude Code → frontend\
Antigravity → backend

Flujo:

Tori → Rosario → bloque negro → agente → integración

------------------------------------------------------------------------

## 17. Principios del sistema

-   UI definida antes de código
-   bloques negros como unidad de ejecución
-   agentes ejecutan, humanos deciden
-   MVP primero

------------------------------------------------------------------------

**Estado:** PRD TORO v0.2 --- Draft operativo completo
