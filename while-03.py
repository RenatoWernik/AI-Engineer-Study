pets = ["cat","dog","fish","cat","dog","cat","rabbit","turtle","cat"]
while "cat" in pets:
    pets.remove("cat")

print(f"Cats were removed from the list:\n{",".join(pets).title()}")
