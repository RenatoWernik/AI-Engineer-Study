people = {
    "renato":{
        "first_name":"renato",
        "middle_name":"freitas",
        "last_name":"wernik",
        "age":23,
        "country":"portugal",
        "city":"lisbon",
        "gender":"male",

    },
    "eduarda":{
        "first_name":"eduarda",
        "middle_name":"paula",
        "last_name":"wernik",
        "age":23,
        "country":"brasil",
        "city":"natal",
        "gender":"female",
    },
    "steve":{
        "first_name":"steve",
        "middle_name":"paul",
        "last_name":"jobs",
        "age":56,
        "country":"usa",
        "city":"san francisco",
        "gender":"male",
    }
}

for person_info in people.values():
    print(f"\nFull name: {person_info['first_name'].title()} {person_info['middle_name'].title()} {person_info['last_name'].title()}")
    if person_info['country'] == "usa":
        print(f"Lives in {person_info['city'].title()} - {person_info['country'].upper()}")
    else:
        print(f"Lives in {person_info['city'].title()} - {person_info['country'].title()}")
    if person_info['gender'] == "male":
        print(f"He is {person_info['age']} years old")
    else:
        print(f"She is {person_info['age']} years old")
