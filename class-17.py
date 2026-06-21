class ModeloLLM:
    def __init__(self,nome,max_tokens):
        self.nome = nome
        self.max_tokens = max_tokens

    def gerar_resposta(self,prompt):
        print(f"{self.nome.title()} gerando resposta para: {prompt}")

    def descrever(self):
        print(f"Limite de tokens por modelo:\n{self.nome.title()} - {self.max_tokens}")


class ModeloOpenAI(ModeloLLM):
    def __init__(self,nome,max_tokens,organizacao):
        super().__init__(nome,max_tokens)
        self.organizacao = organizacao

    def gerar_resposta(self,prompt):
        print("Utilizando API da OpenAI")
        super().gerar_resposta(prompt)

class ModeloAnthropic(ModeloLLM):
    def __init__(self,nome,max_tokens,versao):
        super().__init__(nome,max_tokens)
        self.versao = versao

    def gerar_resposta(self,prompt):
        print("Utilizando a API da Anthropic")
        super().gerar_resposta(prompt)




gpt_5_5 = ModeloOpenAI("gpt 5.5",100_000,"org interna")
gpt_5_5.gerar_resposta("Qual a capital da italia?")
gpt_5_5.descrever()

opus_4_8 = ModeloAnthropic("opus 4.8",300_000,4.8)
opus_4_8.gerar_resposta("Qual o pais com mais copas do mundo?")
opus_4_8.descrever()