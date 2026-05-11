def book_hotel(order_dict: dict):
    print("📦 Hotel booked")
    print(order_dict)

    return {
        "status": "ok",
        "order_id": "12345"
    }