from utilidades.juntar import juntar_falas

def test_lista_vazia(lista_suja_de_exemplo):
    lista_resultado = juntar_falas(lista_suja_de_exemplo)
    assert lista_resultado
    


