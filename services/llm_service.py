import json
from gigachat.models import Chat
from gigachat import GigaChat


# Вставь свой токен
TOKEN = "MDE5ZTExOGYtODI3NS03NmRlLWI1OGEtYjg1YTNlNjkzYjYyOjU5ZTA1NmRiLWEyNGQtNGQzMC1iZDg4LWM5NWRkMGU1NDAzYg=="


client = GigaChat(
    credentials=TOKEN,
    verify_ssl_certs=False
)


SYSTEM_PROMPT = """
Ты система извлечения заказов.

Верни ТОЛЬКО JSON строго формата:

{
  "intent": "create_order",
  "items": [
    {
      "name": "string",
      "quantity": number | null
    }
  ],
  "delivery_location": string | null
}

Никакого текста, объяснений, markdown.
"""


def extract_order(text: str) -> dict:
    response = client.chat(
        Chat(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text}
            ]
        )
    )

    content = response.choices[0].message.content

    return json.loads(content)