from services.llm_service import extract_order
from services.validation_service import validate_create_order
from services.followup import make_question
from services.order_service import submit_order

from schemas.order import CreateOrderSchema


def process_message(text: str):

    raw = extract_order(text)
    
    order = CreateOrderSchema(**raw)
    
    result = validate_create_order(order)
    
    if not result["is_complete"]:
        question = make_question(result["missing_fields"])
        return {
            "status": "need_more_info",
            "message": question,
            "order_state": order.model_dump()
        }
    
    response = submit_order(order.model_dump())
    return {
        "status": "submitted",
        "result": response
    }

print(process_message('Добрый день, хочу сделать заказ: 5 кофе и 10 пачек печенья в офис'))