print("----new contact entry----")
name = input("Name : ")
phone = input("Phone : ")
email = input("Email : ")

with open("contacts.txt", "a") as f:
    f.write(f"{name} , {phone} , {email}\n")

print(f"Contact {name} saved successfully!")
print("---saved contact----")
print(f"Name: {name}")
print(f"Phone: {phone}")
print(f"Email : {email}")
print("-" * 40)

