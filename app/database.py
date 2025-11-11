# db.py
import asyncio
import aiosqlite
from typing import Any, Dict, List, Optional, Tuple
from pydantic import BaseModel as PydanticModel
from fastapi import HTTPException
from traceback import print_stack
import os 
from dotenv import load_dotenv



load_dotenv()

# Environment variable or fallback
DB_PATH = os.getenv("DB_URL", "/home/katyayani/Desktop/Personal/Online-Compiler/app.db")


# Global DB connection (we keep one persistent connection)
_db_connection: Optional[aiosqlite.Connection] = None
_db_lock = asyncio.Lock()  # to prevent race conditions



DB_FILE = "app.db"


_db_connection = None

async def connect_to_db():
    global _db_connection
    if _db_connection is None:
        _db_connection = await aiosqlite.connect(DB_FILE)
        _db_connection.row_factory = aiosqlite.Row
        print(f"✅ Connected to SQLite DB at: {DB_FILE}")
    return _db_connection

async def disconnect_db():
    """Close the global SQLite connection on shutdown."""
    global _db_connection
    if _db_connection is not None:
        await _db_connection.close()
        _db_connection = None
        print(" Disconnected from SQLite DB")


async def get_db_connection() -> aiosqlite.Connection:
    """Return the existing DB connection."""
    global _db_connection
    if _db_connection is None:
        raise RuntimeError("Database is not connected. Call connect_to_db() first.")
    return _db_connection




async def execute_sql(
    sql: str,
    params: Optional[Dict | Tuple] = None,
    *,
    fetchone: Optional[bool] = None,
    fetchall: bool = True,
    default: Any = None,
    raise_error: bool = True,
    rollback_on_error: bool = True,
    model: Optional[PydanticModel] = None,
) -> Optional[List | Dict | PydanticModel]:
    """
    Execute a SQL query (safe wrapper for SELECT/INSERT/UPDATE/DELETE).
    Auto-handles rollback, fetchone/fetchall, and Pydantic model serialization.
    """
    if fetchone is None:
        fetchone = not fetchall

    async with _db_lock:  # avoid race conditions
        try:
            conn = await connect_to_db()
            async with conn.execute(sql, params or {}) as cursor:
                # Commit if write query
                if any(word in sql.upper() for word in ["INSERT", "UPDATE", "DELETE"]):
                    await conn.commit()

                # If SELECT query
                if cursor.description:
                    columns = [desc[0] for desc in cursor.description]
                    rows = [dict(zip(columns, row)) async for row in cursor]

                    if model:
                        data = [model(**row) for row in rows]
                    else:
                        data = rows

                    return data[0] if fetchone else data

                return default

        except Exception as e:
            print_stack(limit=2)
            if rollback_on_error:
                await conn.rollback()
            if raise_error:
                raise HTTPException(status_code=500, detail=str(e))
            return default

