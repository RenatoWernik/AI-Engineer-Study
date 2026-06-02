favorite_languages = {
    "jen":"python",
    "sarah":"c",
    "edward":"rust",
    "phil":"python",
    "renato":"python",
}
i = 1


print("Here are all the names of the participants: \n")

for name in favorite_languages.keys():
    print(f"{i} - {name.title()}")
    i = i + 1



