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
#arquivo = "dados/transcricao.vtt"

class Orquestrador:
    def __init__(self,cliente):
        self.cliente = cliente
        self.prompt_de_sistema = sys_prompt

         
    def chamar_api(self,entrada):
        try:
            resposta = self.cliente.messages.create(
                model = "claude-haiku-4-5-20251001",
                max_tokens = 10000,
                system = self.prompt_de_sistema,
                messages = [{"role":"user","content":entrada}]
            )
            texto_bruto = resposta.content[0].text
            return texto_bruto

        except APIError as e:
            print(f"Erro com a API: {e}")
            return None
    
    def executar(self,arquivo):
        lista_suja = processar_transcricao(arquivo)
        if not lista_suja: #se a lista vier vazia...
            print("Erro: O arquivo da transcrição veio vazio.")
            return None
        lista_limpa = juntar_falas(lista_suja)
        entrada = formatar_lista(lista_limpa)
        #daqui para cima estamos tratando e limpando o arquivo de input para IA
        #daqui para baixo estamos pegando a resposta(output) da IA,salvamos primeiro em texto_bruto
        texto_bruto = self.chamar_api(entrada)
        if texto_bruto is None: #valida se API funcionou.
            print("Erro: A API não retornou texto válido")
            return None
        
        texto_sem_markdown = remover_markdown(texto_bruto)
        dicionario_final = converter_para_json(texto_sem_markdown)
        if dicionario_final is None:
            print("Não foi possivel converter para JSON")
            return None
        
        return dicionario_final


if __name__ == "__main__":
    chamada = Orquestrador(cl)
    resultado_final = chamada.executar("dados/transcricao.vtt")
    print(resultado_final)






#lista_suja = processar_transcricao(arquivo)
#lista_limpa = juntar_falas(lista_suja)
#texto_final = formatar_lista(lista_limpa)

#print(texto_final)
#print(f"Total de falas antes de juntar: {len(lista_suja)}")
#print(f"\nTotal de falas depois de juntar: {len(lista_limpa)}")
#print(f"\n{lista_limpa[:20]}")
