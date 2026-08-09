import pytest

@pytest.fixture
def lista_suja_de_exemplo():
    dados_falsos = [
        {"pessoa":"ivan","fala":"olá!"},
        {"pessoa":"renato","fala":"tudo bem?"},
        {"pessoa":"renato","fala":"como foi o seu dia?"}
    ]

    return dados_falsos

