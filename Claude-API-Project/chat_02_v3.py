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


def carregar_historico(data_file):
    if os.path.exists(data_file):
        print("Arquivo de memoria ja existe!")
        with open(data_file,"r",encoding="utf-8") as f:
            historico = json.load(f) #Leio o arquivo e jogo para a var "historico"
    else:
        print("Criando novo arquivo de memoria...")
        historico = [] 
    
    return historico


def sliding_window(historico,n_msg):
    historico_copy = historico[-n_msg:]
    if historico_copy and historico_copy[0]["role"] == "assistant":
        historico_copy.pop(0)

    return historico_copy


def chamar_api(historico_copy,client):
    try:
        assistant_answer = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=1000,
            messages=historico_copy
        )
        print(assistant_answer.content[0].text)
        return assistant_answer.content[0].text
    except APIError as e:
        print(f"Erro com a API do Claude,tente novamente. {e}")
        return None
        



def salvar_historico(historico, data_file):
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=4, ensure_ascii=False)



history = carregar_historico(data_file)
print("Digite 'quit' para sair. ")
while loop_key:
    user_msg = input("Mensagem para o Claude: ")
    if user_msg == "quit":
        loop_key = False
    else:
        history.append({"role":"user","content":user_msg})
        history_copy = sliding_window(history,10)
        answer = chamar_api(history_copy,client)
        if answer == None:
            print("Erro com a chamada de API,tente novamente ")
            history.pop()
        else:
            history.append({"role":"assistant","content":answer})
salvar_historico(history,data_file)


