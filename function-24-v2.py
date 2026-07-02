import os
import json

file_data = "function-24.json"
file_to_save = "function-24-results.json"

def read_data(data_to_read):
    content = []
    if os.path.exists(data_to_read):
        try:
            with open(data_to_read,"r",encoding="utf-8") as f:
                content = json.load(f)
        except json.JSONDecodeError:
            print("Arquivo vazio ou JSON inválido.")
            return content
    else:
        print("É necessário criar o arquivo primeiro.")
        return content
    
    return content




def process_data(data_to_process):
    resultados = []
    for item in data_to_process:
        if item["nota"] < 7:
            item["Situação"] = "reprovado"
            resultados.append(item)
        else:
            item["Situação"] = "aprovado"
            resultados.append(item)
    return resultados




def save_data(content_to_save,where_to_save):
    if len(content_to_save) > 0:
        with open(where_to_save,"w",encoding="utf-8") as f:
            json.dump(content_to_save,f,indent=4,ensure_ascii=False)
        print("Data saved successfully")
    else:
        print("No data to save.")

ler = read_data(file_data)
processar = process_data(ler)
save_data(processar,file_to_save)