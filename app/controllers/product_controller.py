from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..services.product_service import ProductService
from ..schemas.product_schema import ProductSchema
from ..db.database import get_db
from ..utils.response_wrapper import api_response

router = APIRouter()

@router.post("/customers/{customer_id}/products")
def create_product(
    customer_id: str, 
    product: ProductSchema, 
    db: Session = Depends(get_db)
):
    service = ProductService(db)
    try:
        # Clean the customer_id - remove quotes and any URL encoding
        clean_customer_id = customer_id.strip("'\"")
        new_product = service.create_product(product, clean_customer_id)
        return api_response(data=new_product, message="Product created successfully")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("")
def get_all_products(db: Session = Depends(get_db)):
    service = ProductService(db)
    products = service.get_all_products()
    return api_response(data=products, message="Products retrieved successfully")
