def city_country(city_name,country_name):
    full_name = f"{city_name},{country_name}"
    return full_name.title()

while True:
    print(f"Where you from? ")
    print(f"(Type 'quit' at any time to quit)")
    city = input("City name: ")
    if city == "quit":
        break
    country = input("Country name: ")
    if country == "quit":
        break
    
    formatted_city_country = city_country(city,country)
print(f"Here are the results: {formatted_city_country}")


