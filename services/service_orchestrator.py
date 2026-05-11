import services.hotel_service as hotel
import services.order_service as order
import services.taxi_service as taxi

def orch_services(intent,model_dump:dict):
    if intent == "create_order":
        return order.submit_order(model_dump)
    if intent == "book_taxi":
        return taxi.submit_taxi(model_dump)
    if intent == "book_hotel":
        return hotel.book_hotel(model_dump)