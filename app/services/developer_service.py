from sqlalchemy.orm import Session, joinedload
from ..models.developer import Developer
from ..schemas.developer_schema import DeveloperSchema

class DeveloperService:
    def __init__(self, db: Session):
        self.db = db

    def create_developer(self, developer: DeveloperSchema):
        if self.db.query(Developer).filter(Developer.email == developer.email).first():
            raise ValueError("Email already registered")
        new_developer = Developer(**developer.dict())
        self.db.add(new_developer)
        self.db.commit()
        self.db.refresh(new_developer)
        return new_developer

    def get_developer_with_tickets(self, developer_id: str):
        developer = self.db.query(Developer).filter(Developer.id == developer_id).first()
        if not developer:
            raise ValueError(f"Developer with id {developer_id} not found")
        return developer

    def get_all_developers(self):
        return self.db.query(Developer).all()

    def delete_developer(self, developer_id: str):
        developer = self.db.query(Developer).options(joinedload(Developer.tickets)).filter(Developer.id == developer_id).first()
        if not developer:
            raise ValueError(f"Developer with id {developer_id} not found")
        
        if developer.tickets:
            raise ValueError(f"Cannot delete developer. Developer has {len(developer.tickets)} assigned tickets.")
        
        self.db.delete(developer)
        self.db.commit()
        return developer
