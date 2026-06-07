users = {
    "aeinstein": {
        "first":"albert",
        "last": "einstein",
        "location": "princeton",

    },

    "mcurie":{
        "first":"marie",
        "last":"curie",
        "location":"paris",

    },

}

for username,user_info in users.items():
    print(f"\nUsername: {username}")
    print(f"Full name: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"Location: {user_info['location'].title()}")


    #Criamos um dicionario "users" 
    #Dentro do dicionario "users" criamos chaves em forma de dicionarios, que foram "aeinstein" e "mcurie"
    #Dentro dessas chaves(que são dicionarios) passamos 3 chaves -> first,last, e location
    
    #para acessar o dicionario de fora(users) usamos o for com dois valores(username e user_info) -> com .items() para devolver chaves e valores
        # username sera associado para a chave(pois vem sempre primeiro)
        # user_info sera associado ao valor(pois vem sempre depois da chave)
        # printamos o username chamando a variavel criado dentro for "username" 
        # printamos o full name chamando: {user_info['first'].title()} + {user_info['last'].title()}
        # printamos o location da mesma forma : {user_info['location'].title()}
        