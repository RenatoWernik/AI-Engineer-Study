import pytest
from structured_v1 import Classificator


@pytest.mark.parametrize("texto_entrada, esperado", [('```json\n{"chave": "valor"}\n```',{"chave":"valor"}),
("isto não é um json {quebrado",None),
('{"chave": "valor"}',{"chave":"valor"})])




def test_clear_text(texto_entrada,esperado):
    tester = Classificator(None)
    resultado = tester.clear_text(texto_entrada)
    assert resultado == esperado
