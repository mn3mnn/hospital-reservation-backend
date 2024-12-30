from fastapi import FastAPI
from app.core.config import settings
from app.core.db import init_db_sync

from app.api.endpoints import router as api_endpoint_router
from fastapi.middleware.cors import CORSMiddleware


def startup():
    """
    Function to run at startup.
    """
    # Initialize the database by creating all tables if they do not exist
    init_db_sync()


app = FastAPI(
    title="Hospital System API",
    description="API for a hospital system",
    version="1.0.0",
)

startup()

# CORS (Cross-Origin Resource Sharing) middleware configuration
origins = [
    # settings.FRONTEND_URL,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


app.include_router(router=api_endpoint_router, prefix=settings.API_PREFIX)


@app.get("/")
async def root():
    return {"message": "Hello World"}
