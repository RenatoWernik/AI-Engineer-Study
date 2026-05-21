inscritos = ["Ana","Bruno","Carla","Diogo","Elena"]
inscritos.remove("Carla")
cancelado = inscritos.pop(1)
inscritos.insert(2,"Filipa")
print(f"Lista atual: {', '.join(inscritos)}\nCancelado: {cancelado}")
