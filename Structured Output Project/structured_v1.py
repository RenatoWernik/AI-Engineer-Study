from anthropic import Anthropic,APIError
from dotenv import load_dotenv
import os
import json

from system_prompt import prompt_sistema
load_dotenv()
client = Anthropic()


#Métodos:
#call_api
#run

class Classificator:
    def __init__(self,client_api):
        self.client_api = client_api
        self.system_prompt = prompt_sistema
    
    def call_api(self,msg):
        try:
            assistant_answer = self.client_api.messages.create(
                model = "claude-opus-4-6",
                max_tokens = 2000,
                system = self.system_prompt,
                messages = [{"role":"user","content":msg}]
            )
            texto_bruto = assistant_answer.content[0].text
            return texto_bruto
        except APIError as e:
            print(f"Error API: {e}")
            return None

    def clear_text(self,texto_bruto):
        try:
            texto_limpo = texto_bruto.strip().removeprefix("```json").removesuffix("```").strip()
            dicionario = json.loads(texto_limpo)
            
        except json.JSONDecodeError:
            dicionario = None

        return dicionario

        
        
        
    def run(self):
        user_msg = input("Insira o conteudo para ser avaliado: ")
        texto_bruto = self.call_api(user_msg)
        if texto_bruto is None:
            print("Erro com a chamada de API")
        else:
            resultado_final = self.clear_text(texto_bruto)
            if resultado_final is None:
                print("Erro com o parsing da resposta do Modelo.")
            else:
                print(resultado_final)
        
if __name__ == "__main__":
    chat = Classificator(client)
    chat.run()



