from pydantic import BaseModel
from typing import Optional


class BookTaxiSchema(BaseModel):
        
    intent: str
    
    arrive: Optional[str] = None
    
    destination: Optional[str] = None
    
    