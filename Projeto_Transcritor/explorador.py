from utilidades.processar_transcricao import processar_transcricao
from utilidades.juntar import juntar_falas
from utilidades.formatar_lista_de_dicionarios import formatar_lista
from configuracoes.system_prompt_transcritor import sys_prompt
from utilidades.limpador import remover_markdown,converter_para_json
from dotenv import load_dotenv
import os
from anthropic import Anthropic,APIError
from utilidades.dados_mock import dados

load_dotenv()
cl = Anthropic()
#arquivo = "dados/transcricao.vtt"

class Orquestrador:
    def __init__(self, cliente, validador_cls=None):
        self.cliente = cliente
        self.prompt_de_sistema = sys_prompt
        self.validador_cls = validador_cls or Validador
    
    def executar(self, arquivo, max_try=3):
        lista_suja = processar_transcricao(arquivo)
        if not lista_suja: #se a lista vier vazia...
            print("Erro: O arquivo da transcrição veio vazio.")
            return None
        lista_limpa = juntar_falas(lista_suja)
        entrada = formatar_lista(lista_limpa)

        mensagens = [{"role": "user", "content": entrada}]

        for tentativa in range(1, max_try + 1):
            print(f"\n--- Tentativa {tentativa} de {max_try} ---")
            try:
                resposta = self.cliente.messages.create(
                    model="claude-haiku-4-5-20251001",
                    max_tokens=10000,
                    system=self.prompt_de_sistema,
                    messages=mensagens
                )
                texto_bruto = resposta.content[0].text
            except APIError as e:
                print(f"Erro com a API: {e}")
                return None

            texto_sem_markdown = remover_markdown(texto_bruto)
            dicionario_final = converter_para_json(texto_sem_markdown)

            if dicionario_final is None:
                mensagem_erro = "O formato retornado não é um JSON válido. Envie apenas o JSON puro."
            else:
                validador = self.validador_cls(dicionario_final)
                erros = validador.validar_tudo()
                if not erros:
                    print("✅ Validação aprovada com sucesso!")
                    return dicionario_final

                lista_de_erros = "\n- " + "\n- ".join(erros)
                mensagem_erro = f"O seu resultado falhou nas seguintes validações:{lista_de_erros}\nPor favor, envie o JSON corrigido mantendo todos os dados."

            print(f"⚠️ Falha na validação. Solicitando correção para a IA...")
            mensagens.append({"role": "assistant", "content": texto_bruto})
            mensagens.append({"role": "user", "content": mensagem_erro})

        print("❌ Limite de tentativas atingido sem sucesso.")
        return None


class Validador:
    def __init__(self, dic_final):
        self.dic_final = dic_final
        self.chaves_principais = ["topicos", "insights", "confianca"]
        self.chaves_topicos = ["nome_topico", "resumo_topico", "tarefas"]
        self.chaves_tarefas = ["descricao_tarefa", "estado", "dono_tarefa", "prazo", "atualizacao_tarefa", "evidencia"]

    def validar_tudo(self):
        erros = []
        # valida chaves principais:
        for chave in self.chaves_principais:
            if chave not in self.dic_final:
                erros.append(f"Falta a chave principal: '{chave}'")

        # se nao tiver topicos, nao continua
        if "topicos" not in self.dic_final or not isinstance(self.dic_final["topicos"], list):
            erros.append("A chave 'topicos' precisa ser uma lista.")
            return erros

        # valida cada topico dentro da lista:
        for i, topico in enumerate(self.dic_final["topicos"]):
            for chave in self.chaves_topicos:
                if chave not in topico:
                    erros.append(f"No topico {i+1}, falta a chave '{chave}'")

            # valida cada tarefa dentro do topico:
            if "tarefas" in topico and isinstance(topico["tarefas"], list):
                for j, tarefa in enumerate(topico["tarefas"]):
                    for chave in self.chaves_tarefas:
                        if chave not in tarefa:
                            erros.append(f"No topico {i+1}, tarefa {j+1}, falta a chave '{chave}'")

        return erros




            
            
        

if __name__ == "__main__":
    chamada = Orquestrador(cl)
    resultado = chamada.executar("dados/transcricao.vtt")
    
    print("\n--- RESULTADO FINAL DO PROCESSAMENTO ---")
    print(resultado)








#lista_suja = processar_transcricao(arquivo)
#lista_limpa = juntar_falas(lista_suja)
#texto_final = formatar_lista(lista_limpa)

#print(texto_final)
#print(f"Total de falas antes de juntar: {len(lista_suja)}")
#print(f"\nTotal de falas depois de juntar: {len(lista_limpa)}")
#print(f"\n{lista_limpa[:20]}")
