name = input("Enter your name : ")
age = int(input("Enter your age : "))
height = float(input("Enter your height : "))
is_developer = input("Enter (True/False) : ").strip().lower()=="true"
hobbies = input("Enter values by space : ").split()
profile = {
    "name": name,
    "age": age,
    "height": height,
    "is_developer": is_developer,
    "hobbies": hobbies
}

print(f"\n---profile---")
print("------------------------------")
print(f"Name : {profile['name']}")
print(f"Age : {profile['age']}")
print(f"Height : {profile['height']}")
print(f"is_developer : {profile['is_developer']}")
print(f"Hobbies : {profile['hobbies']}")

print(f"\n---type checkig---")
print("-------------------")
print(f"name is a {type(name)}")
print(f"age is a {type(age)}")
print(f"height is a {type(height)}")
print(f"is_developer is a {type(is_developer)}")
print(f"hobbies is a {type(hobbies)}")
print(f"profile is a {type(profile)}")