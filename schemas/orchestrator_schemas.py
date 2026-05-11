from pydantic import BaseModel
from typing import Optional

import schemas.booking as booking
import schemas.order as order
import schemas.taxi as taxi

def orch_schemas(text,**raw):
    if text == "create_order":
        return order.CreateOrderSchema(**raw)
    if text == "book_taxi":
        return taxi.BookTaxiSchema(**raw)
    if text == "book_hotel":
        return booking.BookHotelSchema(**raw)
