from utilidades.processar_transcricao import processar_transcricao
from utilidades.juntar import juntar_falas
from utilidades.formatar_lista_de_dicionarios import formatar_lista
from configuracoes.system_prompt_transcritor import sys_prompt
from utilidades.limpador import remover_markdown,converter_para_json
from dotenv import load_dotenv
import os
from anthropic import Anthropic,APIError

load_dotenv()
cl = Anthropic()
arquivo = "dados/transcricao.vtt"

class Orquestrador:
    def __init__(self,cliente):
        self.cliente = cliente
        self.prompt_de_sistema = sys_prompt

         
    def chamar_api(self):
        try:
            resposta = self.cliente.messages.create(
                model = "claude-haiku-4-5-20251001",
                max_tokens = 10000,
                system = self.prompt_de_sistema,
                messages = [{"role":"user","content":self.entrada}]
            )
            texto_bruto = resposta.content[0].text
            return texto_bruto

        except APIError as e:
            print(f"Erro com a API: {e}")
            return None
    
    def executar(self):
        self.lista_suja = processar_transcricao(arquivo)
        self.lista_limpa = juntar_falas(self.lista_suja)
        self.entrada = formatar_lista(self.lista_limpa)
        texto_bruto = self.chamar_api()
        texto_sem_markdown = remover_markdown(texto_bruto)
        dicionario_final = converter_para_json(texto_sem_markdown)
        return dicionario_final



chamada = Orquestrador(cl)
resultado_final = chamada.executar()
print(resultado_final)






#lista_suja = processar_transcricao(arquivo)
#lista_limpa = juntar_falas(lista_suja)
#texto_final = formatar_lista(lista_limpa)

#print(texto_final)
#print(f"Total de falas antes de juntar: {len(lista_suja)}")
#print(f"\nTotal de falas depois de juntar: {len(lista_limpa)}")
#print(f"\n{lista_limpa[:20]}")
