from pydantic import BaseModel
from typing import Optional

class OrderItem(BaseModel):
    
    name: str
    
    quantity: Optional[int] = None
    
    unit: Optional[int] = None
    
    category: Optional[str] = None
    
    url: Optional[str] = None

class CreateOrderSchema(BaseModel):
    
    intent: str
    
    items: list[OrderItem]
    