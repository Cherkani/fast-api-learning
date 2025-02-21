from sqlalchemy.orm import Session, joinedload
from ..models.customer import Customer
from ..models.product import Product
from ..schemas.customer_schema import CustomerSchema, CustomerWithProductsSchema
from ..schemas.product_schema import ProductSchema

class CustomerService:
    def __init__(self, db: Session):
        self.db = db

    def create_customer(self, customer: CustomerSchema):
        if self.db.query(Customer).filter(Customer.email == customer.email).first():
            raise ValueError("Email already registered")
        new_customer = Customer(**customer.dict())
        self.db.add(new_customer)
        self.db.commit()
        self.db.refresh(new_customer)
        return new_customer

    def get_customer_with_products(self, customer_id: str):
        # Use joinedload to eagerly load products
        customer = (
            self.db.query(Customer)
            .options(joinedload(Customer.products))
            .filter(Customer.id == customer_id)
            .first()
        )
        if not customer:
            raise ValueError("Customer not found")
        return CustomerWithProductsSchema(
            id=customer.id,
            name=customer.name,
            email=customer.email,
            address=customer.address,
            products=[ProductSchema(name=p.name, price=p.price) for p in customer.products]
        )

    def get_all_customers(self):
        return self.db.query(Customer).all()
