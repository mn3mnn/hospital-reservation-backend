from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings

from app.core.all_db_models import SQLBase

# Create async engine for async operations
async_engine = create_async_engine(
    settings.DATABASE_URL_ASYNC,
    echo=True,
    future=True
)

# Create sync engine for sync operations
sync_engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)

# Use session maker for async session
AsyncSessionLocal = sessionmaker(
    bind=async_engine,  # Bind the async engine
    class_=AsyncSession,
    expire_on_commit=False
)

# Use session maker for sync session
SyncSessionLocal = sessionmaker(
    bind=sync_engine,  # Bind the sync engine
    # class_=Session,
    # expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

async def init_db_async():
    """
    Initialize the database for async operations by creating all SQLBase tables if they do not exist.
    This function must be async when using async SQLAlchemy.
    """
    async with async_engine.begin() as conn:
        # Create tables based on SQLBase models in all_db_models.py
        await conn.run_sync(SQLBase.metadata.create_all)
        await conn.commit()

def init_db_sync():
    """
    Initialize the database for sync operations by creating all SQLBase tables if they do not exist.
    This function must be sync when using sync SQLAlchemy.
    """
    # Create schemas if they don't exist
    with sync_engine.connect() as conn:
        # Create tables based on SQLBase models
        SQLBase.metadata.create_all(conn)

        conn.commit()

# Async function to get async session
async def get_db_async() -> AsyncSession:
    """
    Dependency function to get the async database session
    @return: AsyncSession
    """
    async with AsyncSessionLocal() as session:
        yield session

# Sync function to get sync session
def get_db_sync() -> Session:
    """
    Dependency function to get the sync database session
    @return: Session
    """
    return SyncSessionLocal()
