from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..services.developer_service import DeveloperService
from ..schemas.developer_schema import DeveloperSchema, DeveloperWithTicketsSchema
from ..db.database import get_db
from ..utils.response_wrapper import api_response

router = APIRouter()

@router.post("")
def create_developer(developer: DeveloperSchema, db: Session = Depends(get_db)):
    service = DeveloperService(db)
    try:
        new_developer = service.create_developer(developer)
        return api_response(data=new_developer, message="Developer created successfully")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{developer_id}", response_model=DeveloperWithTicketsSchema)
def get_developer_with_tickets(developer_id: str, db: Session = Depends(get_db)):
   
    cleaned_id = developer_id.strip('"\'')
    service = DeveloperService(db)
    try:
        developer = service.get_developer_with_tickets(cleaned_id)
        if not developer:
            raise HTTPException(status_code=404, detail="Developer not found")
        return developer
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("")
def get_all_developers(db: Session = Depends(get_db)):
    service = DeveloperService(db)
    developers = service.get_all_developers()
    return api_response(data=developers, message="Developers retrieved successfully")

@router.delete("/{developer_id}")
def delete_developer(developer_id: str, db: Session = Depends(get_db)):
    service = DeveloperService(db)
    try:
        cleaned_id = developer_id.strip('"\'')
        deleted_developer = service.delete_developer(cleaned_id)
        return api_response(
            data=deleted_developer,
            message="Developer deleted successfully"
        )
    except ValueError as e:
        if "Cannot delete developer" in str(e):
            raise HTTPException(status_code=400, detail=str(e))
        raise HTTPException(status_code=404, detail=str(e))
