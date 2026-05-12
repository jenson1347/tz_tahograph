def submit_order(order_dict: dict):
    print("📦 ORDER SUBMITTED:")
    print(order_dict)

    return {
        "API_response": "заказ создан",
        "status": "ok",
        "order_id": "12345"
    }