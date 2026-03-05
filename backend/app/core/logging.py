import logging
import sys
from app.core.settings import settings

def setup_logging():
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Disable excessive logs from some libraries
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    
setup_logging()
logger = logging.getLogger("argos")
