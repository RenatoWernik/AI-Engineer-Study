import json
def remover_markdown(texto_bruto):
    texto_limpo = texto_bruto.strip().removeprefix("```json").removesuffix("```").strip()
    return texto_limpo

def converter_para_json(texto_limpo):
    try:
        dicionario_limpo = json.loads(texto_limpo)
    except json.JSONDecodeError:
        dicionario_limpo = None
    return dicionario_limpo