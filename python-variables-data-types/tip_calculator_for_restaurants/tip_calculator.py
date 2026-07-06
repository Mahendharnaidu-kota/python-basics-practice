#Tip Calculator for Restaurants
bill_amount = float(input("Enter the bill amount : "))
tip_percentage = float(input("Enter tip percentage : "))
number_of_people = int(input("Enter num of people : "))

tip_amount = bill_amount * (tip_percentage / 100)

per_person_payment = (bill_amount + tip_amount) / number_of_people

GREEN = "\033[92m"
RESET = "\033[0m"

print(f"{GREEN} Tip Calculator {RESET}")
print("------------------")
print(f"Bill Amount : ${bill_amount:.2f}")
print(f"Tip percentage : {tip_percentage} %")
print(f"Num of People : {number_of_people}")
print(f"Tip amount : ${tip_amount}")
print(f"{GREEN}Per person payment : ${per_person_payment}{RESET}")