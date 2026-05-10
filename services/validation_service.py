from schemas.order import CreateOrderSchema


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
    
    if not order.delivery_location:

        missing_fields.append(
            "delivery_location"
            )


    return {
        "is_complete": len(missing_fields) == 0,
        "missing_fields": missing_fields
    }        