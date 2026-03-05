# ARGOS Backend

Market analysis engine and API for the TORO ecosystem.

## Stack
- Python 3.11+
- FastAPI
- PostgreSQL (SQLAlchemy)
- Pandas/NumPy
- APScheduler

## Project Structure
- `app/core/`: Configuration and logging.
- `app/db/`: Database models and session management.
- `app/analyzers/`: Technical analysis logic (RSI, MACD, etc.).
- `app/data/`: External data providers (Finnhub).
- `app/routes/`: API endpoints.
- `app/jobs/`: Background tasks.

## Setup

1. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables:**
   - Copy `.env.example` to `.env`.
   - Update `FINNHUB_API_KEY` and `DATABASE_URL`.

4. **Run Application:**
   ```bash
   cd backend
   uvicorn app.main:app --reload --port 8000
   ```

## API Documentation
Once running, visit:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Health Check: [http://localhost:8000/api/health](http://localhost:8000/api/health)
