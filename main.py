from services.llm_service import extract
from services.validation_service import orch_validate
from services.followup import make_question
from services.service_orchestrator import orch_services
from schemas.orchestrator_schemas import orch_schemas


def process_message(text: str):

    raw = extract(text)
    
    order = orch_schemas(raw['intent'],**raw)
    
    result = orch_validate(raw['intent'],order)
    
    print(raw["intent"])
    
    if not result["is_complete"]:
        question = make_question(result["missing_fields"])
        return {
            "status": "need_more_info",
            "message": question,
            "order_state": order.model_dump()
        }
    
    response = orch_services(raw['intent'],order.model_dump())
    return {
        "status": "submitted",
        "result": response
    }

print(process_message('Забронируй мне отель в Москве'))