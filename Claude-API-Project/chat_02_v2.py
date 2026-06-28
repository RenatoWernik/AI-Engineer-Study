#Importando as classes "Anthropic" e "APIError" da biblioteca "anthropic" 
from anthropic import Anthropic,APIError
#Importando função "load_dotenv" da biblioteca "dotenv"
from dotenv import load_dotenv
#Importando biblioteca completa "os"
import os

#Importando biblioteca completa do "Json" para usar dump e read.
import json

#Tentativa de fazer uma ligação a API da Anthropic para usar o Claude e guardar/ler
#um arquivo separado chamado "data.json" para usar como memoria persistente do Claude"""

load_dotenv()

client = Anthropic()

data_file = "data.json"

loop_key = True



print("Digite 'quit' para sair. ")

if os.path.exists(data_file):
    print("Arquivo de memória ja existe\nIniciando chamada da API... ")
    with open(data_file,"r",encoding="utf-8") as f: 
        historico = json.load(f) #Historico adicionado na memória.
else:
    print("Criando nova memória... ")
    historico = [] # Se não existe o arquivo,inicia uma lista vazia.


while loop_key:
    user_msg = input("Mensagem para o Claude: ")
    if user_msg == "quit":
        loop_key = False
    else:
        #Adicionar a o prompt atual do user para o histórico
        historico.append({"role":"user","content":user_msg})
        historico_copy = historico[-10:]
        if historico_copy[0]["role"] == "assistant":
            historico_copy.pop(0)
            .
        try:
            #Chamada da API com historico atualizado do ultimo prompt
            assistant_answer = client.messages.create(
                model = "claude-opus-4-6",
                max_tokens = 1000,
                messages = historico_copy
            )
        except APIError as e:
            print(f"Erro com a API do Claude,tente novamente. {e}")
            historico.pop()

        else:

            #Exibir a resposta para o user.
            print(assistant_answer.content[0].text)
            #Adicionar a resposta do assistant para o historico.
            historico.append({"role":"assistant","content":assistant_answer.content[0].text})

with open(data_file,"w",encoding ="utf-8") as f:
    #Passando conversa completa para o arquivo json.
    json.dump(historico,f,indent=4,ensure_ascii=False)       