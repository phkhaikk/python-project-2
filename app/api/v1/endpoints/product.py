import json
from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from starlette import status
from redis import Redis

from app import crud, models, schemas
from app.crud.crud_product import product as crud_product
from app.schemas.product import ProductDb, ProductCreate, ProductUpdate
from app.api import deps

from app.core.config import settings
from app.core.exception_handler import CustomException
from app.schemas.base import DataResponse
from app.utils import send_new_account_email

router = APIRouter()

redis_client = Redis(host='localhost', port=6379,db=0)

@router.get("/", response_model=List[ProductDb])
def read_all_products(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 10):
    db_product = crud_product.get_products(db=db, skip=skip, limit=limit)
    return db_product


@router.get("/{product_id}", response_model=ProductDb)
def read_product_by_id(product_id: int, db: Session = Depends(deps.get_db)):
    db_product = crud_product.get_product_by_id(product_id=product_id, db=db)
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return db_product


@router.post("/", response_model=ProductDb)
def create_product(product: ProductCreate, db: Session = Depends(deps.get_db)):
    db_product = crud_product.get_product_by_name(name=product.name, db=db)
    if db_product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product already exists")
    return crud_product.create_product(db=db, obj_in=product)


@router.put("/{product_id}", response_model=ProductDb)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(deps.get_db)):
    db_product = crud_product.get_product_by_id(db=db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return crud_product.update_product(db=db, db_product=db_product, obj_in=product)


@router.delete("/{product_id}", response_model=ProductDb)
def delete_product(product_id: int, db: Session = Depends(deps.get_db)):
    db_product = crud_product.get_product_by_id(db=db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    crud_product.delete_product(db=db, product_id=product_id)
    return db_product
