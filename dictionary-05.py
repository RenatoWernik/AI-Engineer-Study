#Exercício: Convite para um Clube de Programação

favorite_lang = {
    "jen":"python",
    "sarah":"c",
    "edward":"rust",
    "phil":"python",
    "renato":"python",
    "ana":"java",
}

registered = ["phil","ana"]

i = 1

for name in favorite_lang.keys():
    if name in registered:
        print(f"{i} - {name.title()} -> Already registered")
        
    else:
        print(f"{i} - {name.title()} -> Invitation sent")
    i += 1  

python = 0
for py in favorite_lang.values():
    if py == "python":
        python += 1
print(f"\nTotal python lovers: {python}")

lang_count = {}
for lang in favorite_lang.values():
    if lang not in lang_count:
        lang_count[lang] = 1
    else:
        lang_count[lang] += 1
    
most_popular = max(lang_count, key=lang_count.get)

if most_popular == "python":
    print("The most popular language is still python")
else:
    print(f"The most popular language is: {most_popular}")




