from anthropic import Anthropic
from dotenv import load_dotenv
import os




load_dotenv()
client = Anthropic()

loop_key = True
historico = []


print("Digite 'quit' para sair")

   

while loop_key:
    user_msg = input("Mensagem para o Clude: ")
    if user_msg == "quit":
        loop_key = False
    else:
        historico.append({"role":"user","content":user_msg})
        resposta = client.messages.create(
        model = "claude-opus-4-6",
        max_tokens = 1000,
        messages= historico

    )
        print(resposta.content[0].text)
        historico.append({"role":"assistant","content":resposta.content[0].text})


 



