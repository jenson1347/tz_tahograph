from pydantic import BaseModel
from typing import Optional

class BookHotelSchema(BaseModel):
    
    intent: str
    
    persona: Optional[str] = None
    
    guests: Optional[int] = None
    
    country: Optional[str] = None

    city: Optional[str] = None

    date_in: Optional[str] = None

    date_out: Optional[str] = None
