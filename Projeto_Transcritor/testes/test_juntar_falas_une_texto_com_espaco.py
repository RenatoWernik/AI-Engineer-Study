from utilidades.juntar import juntar_falas
def test_juntar_falas_consecutivas_2(lista_suja_de_exemplo):
    resultado_falas = juntar_falas(lista_suja_de_exemplo)
    assert resultado_falas[1] == {'fala': 'tudo bem? como foi o seu dia?', 'pessoa': 'renato'}
        
        