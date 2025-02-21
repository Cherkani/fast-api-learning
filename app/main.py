

from fastapi import FastAPI
from .controllers.customer_controller import router as customer_router
from .controllers.product_controller import router as product_router


app = FastAPI(
    title="Customer and Product Management API",
    description="A CRUD API for managing customers and their products.",
    version="1.0.0",
)


app.include_router(customer_router, prefix="/api/customers", tags=["Customers"])


app.include_router(product_router, prefix="/api/products", tags=["Products"])


@app.get("/")
def root():
    return {"message": "Welcome to the Customer and Product Management API!"}
