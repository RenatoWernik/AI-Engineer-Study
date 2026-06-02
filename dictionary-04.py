favorite_languages = {
    "jen":"python",
    "sarah":"c",
    "edward":"rust",
    "phil":"python",
    "renato":"python",
}

friends = ["phil","sarah"]
for name in favorite_languages.keys():
    if name in friends:
        print(f"Hi {name.title()}, i see you love {favorite_languages[name]}")
    else:
        print(f"Hi {name}")
    

