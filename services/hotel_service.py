def book_hotel(order_dict: dict):
    print("📦 Hotel booked")
    print(order_dict)

    return {
        "API_response": "Отель забронирован",
        "status": "ok",
        "order_id": "12345"
    }