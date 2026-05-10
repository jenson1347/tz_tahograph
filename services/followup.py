from gigachat import GigaChat


TOKEN = "MDE5ZTExOGYtODI3NS03NmRlLWI1OGEtYjg1YTNlNjkzYjYyOjU5ZTA1NmRiLWEyNGQtNGQzMC1iZDg4LWM5NWRkMGU1NDAzYg=="
client = GigaChat(credentials=TOKEN, verify_ssl_certs=False)


def make_question(missing_fields: list[str]) -> str:

    prompt = f"""
У пользователя не хватает данных для заказа:

{missing_fields}

Сформируй короткий уточняющий вопрос.
"""

    response = client.chat(
        prompt
    )

    return response.choices[0].message.content