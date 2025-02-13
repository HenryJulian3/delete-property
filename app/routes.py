from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import Property
from .schemas import PropertyDeleteResponse

router = APIRouter()

@router.delete("/delete/{property_id}", response_model=PropertyDeleteResponse)
def delete_property(property_id: int, db: Session = Depends(get_db)):
    # Buscar la propiedad en la base de datos
    property_record = db.query(Property).filter(Property.id == property_id).first()
    
    if not property_record:
        raise HTTPException(status_code=404, detail="Property not found")
    
    # Eliminar la propiedad
    db.delete(property_record)
    db.commit()
    
    return {"message": "Property deleted successfully"}
