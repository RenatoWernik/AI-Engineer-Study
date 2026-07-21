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
my_anthropic = Anthropic() #passo essa variavel como argumento de "client_api" ao chamar a classe.



class AIChat:
    def __init__(self,client_api,history_file="data.json"):
        
        self.client_api = client_api
        self.history_file = history_file
        self.history = self.load_history() # -> Metodo

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file,"r",encoding="utf-8") as f:
                try:
                    content = json.load(f) # Ler o arquivo - TRAZER para o Python
                except json.JSONDecodeError:
                    print("Aviso: O arquivo de histórico está corrompido ou vazio. Iniciando um novo chat limpo.")
                    content = []
        else:
            print("É necessario criar o arquivo primeiro.")
            content = []
        return content #conteudo do arquivo em formato correto para o python usar no init com self.history
            
       

    def call_api(self):
        sliced_history = self.sliding_window(10)
        try:
            assistant_answer = self.client_api.messages.create(
                model="claude-opus-4-6",
                max_tokens=1000,
                messages=sliced_history
            )
            return assistant_answer.content[0].text
        except APIError as e:
            print(f"Erro com a API do Claude,tente novamente. {e}")
            return None
            
    def save_history(self):
        with open(self.history_file,"w",encoding="utf-8") as f:
            json.dump(self.history,f,indent=4,ensure_ascii=False)
        

    def run(self):
        loop_key = True
        print("Digite 'quit' para sair. ")
        while loop_key:
            user_msg = input("Mensagem para o Claude: ")
            if user_msg.lower() == "quit":
                loop_key = False
            else:
                self.history.append({"role":"user","content":user_msg})
                answer = self.call_api()
                if answer is None:
                    print("A API falhou,desfazendo a mensagem...")
                    self.history.pop()
                else:
                    print(answer)
                    self.history.append({"role":"assistant","content":answer})
        self.save_history()

                
        

    def sliding_window(self,n_msg=10):
        history_copy = self.history[-n_msg:]
        if history_copy and history_copy[0]["role"] == "assistant":
            history_copy.pop(0)
        return history_copy
       
        

chat = AIChat(my_anthropic)
chat.run()




