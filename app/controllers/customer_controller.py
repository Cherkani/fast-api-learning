from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..services.customer_service import CustomerService
from ..schemas.customer_schema import CustomerSchema, CustomerWithProductsSchema
from ..db.database import get_db
from ..utils.response_wrapper import api_response

router = APIRouter()

@router.post("")
def create_customer(customer: CustomerSchema, db: Session = Depends(get_db)):
    service = CustomerService(db)
    try:
        new_customer = service.create_customer(customer)
        return api_response(data=new_customer, message="Customer created successfully")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{customer_id}", response_model=CustomerWithProductsSchema)
def get_customer_with_products(customer_id: str, db: Session = Depends(get_db)):
    service = CustomerService(db)
    try:
        # Clean the customer_id - remove quotes and any URL encoding
        clean_customer_id = customer_id.strip("'\"")
        customer = service.get_customer_with_products(clean_customer_id)
        return customer  
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("")
def get_all_customers(db: Session = Depends(get_db)):
    service = CustomerService(db)
    customers = service.get_all_customers()
    return api_response(data=customers, message="Customers retrieved successfully")
