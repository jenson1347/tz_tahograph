def submit_taxi(order_dict: dict):
    print("📦 TAXI SUBMITTED:")
    print(order_dict)

    return {
        "API_response": "Такси вызвано",
        "status": "ok",
        "order_id": "12345"
    }