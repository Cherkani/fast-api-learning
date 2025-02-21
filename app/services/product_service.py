from sqlalchemy.orm import Session
from ..models.product import Product
from ..models.customer import Customer
from ..schemas.product_schema import ProductSchema

class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product: ProductSchema, customer_id: str):
        # Check if customer exists
        customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        if not customer:
            raise ValueError(f"Customer with ID {customer_id} not found")
        
        # Create new product
        new_product = Product(
            name=product.name,
            price=product.price,
            owner_id=customer_id
        )
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product

    def get_all_products(self):
        return self.db.query(Product).all()
