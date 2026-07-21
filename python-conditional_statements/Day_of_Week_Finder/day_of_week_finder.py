# Day of week finder

print("*" * 50)
print("---Day of Week Finder---")
print("*" * 50)

user_input = input("Enter a number (1-7) or a day name: ").strip().capitalize()

# ---- Determine if input is numeric or a day name ----
if user_input.isdigit():
    num = int(user_input)

    if num == 1:
        day = "Monday"
    elif num == 2:
        day = "Tuesday"
    elif num == 3:
        day = "Wednesday"
    elif num == 4:
        day = "Thursday"
    elif num == 5:
        day = "Friday"
    elif num == 6:
        day = "Saturday"
    elif num == 7:
        day = "Sunday"
    else:
        day = "Invalid number. Enter a valid number between 1-7"

else:
    if user_input == "Monday":
        num, day = 1, "Monday"
    elif user_input == "Tuesday":
        num, day = 2, "Tuesday"
    elif user_input == "Wednesday":
        num, day = 3, "Wednesday"
    elif user_input == "Thursday":
        num, day = 4, "Thursday"
    elif user_input == "Friday":
        num, day = 5, "Friday"
    elif user_input == "Saturday":
        num, day = 6, "Saturday"
    elif user_input == "Sunday":
        num, day = 7, "Sunday"
    else:
        num, day = None, "Invalid day name. Enter a valid day (Monday-Sunday)"

# ---- Weekend / Weekday classification ----
if day in ("Saturday", "Sunday"):
    category = "Weekend"
elif day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    category = "Weekday"
else:
    category = "N/A"

# ---- Output ----
print()
if num is not None and 1 <= num <= 7:
    print(f"Day number : {num}")
    print(f"Day name   : {day}")
    print(f"Category   : {category}")
else:
    print(day)

print("*" * 50)