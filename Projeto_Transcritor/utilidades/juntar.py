import json
def juntar_falas(lista_suja):
    
    lista_otimizada = []

    for item in lista_suja:
        if not lista_otimizada or item["pessoa"] != lista_otimizada[-1]["pessoa"]:
            lista_otimizada.append({"pessoa":item["pessoa"],"fala":item["fala"]})
        else:
            lista_otimizada[-1]["fala"] += " " + item["fala"]

    return lista_otimizada





    
        
          