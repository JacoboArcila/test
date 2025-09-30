
from typing import List
import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

DB_PATH = "test.db"

app = FastAPI(title="Products API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProductIn(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., ge=0)

class Product(ProductIn):
    id: int

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    ## ----------------- ##
    # Crea la tabla de products
    ## ----------------- ##

    # seed
    cur.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] == 0:
        cur.executemany(
            ## ----------------- ##
            # Insertar products
            ## ----------------- ##
        )

    conn.commit()
    conn.close()

init_db()

def rows_to_products(rows):
    return [ {"id": r[0], "name": r[1], "price": r[2]} for r in rows ]

## ----------------- ##
    # Crea EndPoint, obtener productos
## ----------------- ##

## EXTRA ----------------- ##
    # Crea EndPoint, Agregar Productos
## ----------------- ##
