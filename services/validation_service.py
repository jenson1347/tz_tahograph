from schemas.order import CreateOrderSchema
from schemas.taxi import BookTaxiSchema
from schemas.booking import BookHotelSchema


def orch_validate(text,order):
    if text == "create_order":
        return validate_create_order(order)
    if text == "book_taxi":
        return validate_book_taxi(order)
    if text == "book_hotel":
        return validate_book_hotel(order)



def validate_create_order(
    order: CreateOrderSchema
):

    missing_fields = []
    if not order.items:
        missing_fields.append("items")
    
    
    for item in order.items:

        if item.quantity is None:

            missing_fields.append(
                f"quantity:{item.name}")

    return {
        "is_complete": len(missing_fields) == 0,
        "missing_fields": missing_fields
    }

def validate_book_taxi(
    order: BookTaxiSchema
):

    missing_fields = []
    if not order.arrive:
        missing_fields.append("arrive")
    
    if not order.destination:
        missing_fields.append("destination")


    return {
        "is_complete": len(missing_fields) == 0,
        "missing_fields": missing_fields
    }

def validate_book_hotel(
    order: BookHotelSchema
):

    missing_fields = []
    if not order.persona:
        missing_fields.append("persona")
    if not order.guests:
        missing_fields.append("guests")
    if not order.country:
        missing_fields.append("country")
    if not order.city:
        missing_fields.append("city")
    if not order.date_in:
        missing_fields.append("date_in")
    if not order.date_out:
        missing_fields.append("date_out")

    return {
        "is_complete": len(missing_fields) == 0,
        "missing_fields": missing_fields
    }


