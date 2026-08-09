from utilidades.juntar import juntar_falas

def test_juntar_falas_consecutivas(lista_suja_de_exemplo): #nome da fixture -> lista_suja_de_exemplo

    resultado = juntar_falas(lista_suja_de_exemplo)

    assert len(resultado) == 2

