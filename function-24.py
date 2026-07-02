import os
import json
#O problema: construa um programa pequeno que processe uma lista de dados de um arquivo
#Primeiro, carregar os dados de um arquivo JSON. Se o arquivo não existir ou estiver vazio, o programa não pode quebrar, tem que lidar com isso
#Segundo, processar os dados de alguma forma que exija lógica
#Terceiro, salvar o resultado processado num novo arquivo JSON.
file = "function-24.json"
to_save = "function-24-results.json"
def load_file(file_to_load):
    if os.path.exists(file_to_load):
        with open(file_to_load,"r",encoding="utf-8") as f:
            content = json.load(f)
            
    else:
        print("É necessario criar o arquivo primeiro.") #como crio o arquivo automaticamente quando ele ainda não existe?
    return content
#Preciso encontrar uma forma de usar Try/Except para caso o arquivo não exista ou esteja vazio

def process_data(file_to_load):
    data_to_process = load_file(file_to_load)
    resultados = []
    for item in data_to_process:
        if item["nota"] < 7:
            aluno = f"Aluno {item["nome"]} reprovado com nota {item["nota"]}"
            resultados.append(aluno)
        else:
            aluno = f"Aluno {item["nome"]} aprovado com nota {item["nota"]}"
            resultados.append(aluno)
    return resultados

def save_data(file_to_save):
    data_to_save = process_data(file)
    with open(file_to_save,"w",encoding="utf-8") as f:
        json.dump(data_to_save,f,indent=4,ensure_ascii=False)
    print("File saved,check it out.")
    

save_data(to_save)

