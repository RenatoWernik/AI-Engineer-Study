
from structured_v1 import Classificator

def test_clear_text_json_valido():
    # Planejar
    texto_entrada = '```json\n{"chave": "valor"}\n```'
    tester = Classificator(None)

    #Agir
    resultado = tester.clear_text(texto_entrada)

    #Validar
    assert resultado == {"chave":"valor"}




def test_clear_text_json_invalid():
    input_text = 'isto não é um json {quebrado'
    instance_tester = Classificator(None)
    output = instance_tester.clear_text(input_text)
    assert output is None