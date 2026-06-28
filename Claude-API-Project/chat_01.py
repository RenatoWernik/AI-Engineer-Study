from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = Anthropic()




resposta = client.messages.create(
    model = "claude-opus-4-6",
    max_tokens = 1000,
    messages= [
        {"role": "user", "content": "Olá! Quem é você?"}
    ]
)

print(resposta.content[0].text)

