import json
from gigachat.models import Chat
from gigachat import GigaChat
from router.router import route
from prompts.sys_prompt import orchestrator_prompts

# Вставь свой токен
TOKEN = "MDE5ZTExOGYtODI3NS03NmRlLWI1OGEtYjg1YTNlNjkzYjYyOjU5ZTA1NmRiLWEyNGQtNGQzMC1iZDg4LWM5NWRkMGU1NDAzYg=="


client = GigaChat(
    credentials=TOKEN,
    verify_ssl_certs=False
)


def extract(text: str) -> dict:
    
    result = route(text)
    print(f"ROUTER ANSWER: {result['intent']}")

    SYSTEM_PROMPT = orchestrator_prompts[result['intent']]

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