from schemas.order import CreateOrderSchema,OrderItem
from services.validation_service import validate_create_order


item1 = OrderItem(
    name = 'Кофе',
    quantity=10 
)
item2 = OrderItem(
    name = 'чай',
    quantity=20 
)

order = CreateOrderSchema(
    intent = 'create_order',
    items = [item1,item2]
    
)

print(validate_create_order(order))

from gigachat import GigaChat


# Вставь свой токен
TOKEN = "MDE5ZTExOGYtODI3NS03NmRlLWI1OGEtYjg1YTNlNjkzYjYyOjU5ZTA1NmRiLWEyNGQtNGQzMC1iZDg4LWM5NWRkMGU1NDAzYg=="


client = GigaChat(
    credentials=TOKEN,
    verify_ssl_certs=False
)


response = client.chat(
    "Привет! Ответь коротко."
)

print(response.choices[0].message.content)