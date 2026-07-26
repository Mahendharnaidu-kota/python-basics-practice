# ATM Withdrawal System
print("*" * 50)
print("---ATM Withdrawal System---")
print("*" * 50)

bank_balance = 50000
security_pin = 9493
mini_statement = []
daily_limit = 20000
remaining_daily_limit = daily_limit

operation = input("Enter your operation : ").strip().lower()

if operation not in ("withdrawal", "deposit", "check balance", "mini statement", "change pin"):
    print("Enter valid operation in (withdrawal, deposit, check balance, mini statement, change pin)")

elif operation == "withdrawal":
    amount = int(input("Enter withdrawal amount : "))
    pin = int(input("Enter security pin : "))

    if pin != security_pin:
        print("Invalid PIN")
    elif amount <= 0:
        print("Enter an amount greater than zero")
    elif amount % 100 != 0:
        print("Amount should be in multiples of 100")
    elif amount > bank_balance:
        print("Insufficient funds, please enter a valid amount")
    elif amount > remaining_daily_limit:
        print(f"Amount exceeds remaining daily limit of {remaining_daily_limit}")
    else:
        bank_balance -= amount
        remaining_daily_limit -= amount
        mini_statement.append(f"Withdrawal: {amount}")

        # Denomination breakdown using only arithmetic (no loops)
        notes_2000 = amount // 2000
        remainder = amount % 2000
        notes_500 = remainder // 500
        remainder = remainder % 500
        notes_200 = remainder // 200
        remainder = remainder % 200
        notes_100 = remainder // 100

        print(f"Withdrawal of {amount} is successful")
        print(f"Balance amount = {bank_balance}")
        print(f"Remaining daily limit = {remaining_daily_limit}")
        print("Denomination breakdown:")
        if notes_2000 > 0:
            print(f"  2000 x {notes_2000}")
        if notes_500 > 0:
            print(f"  500  x {notes_500}")
        if notes_200 > 0:
            print(f"  200  x {notes_200}")
        if notes_100 > 0:
            print(f"  100  x {notes_100}")

elif operation == "deposit":
    print("Cash or cheque deposit machine is upgrading for this feature. Coming soon ----")

elif operation == "check balance":
    pin = int(input("Enter security pin : "))
    if pin == security_pin:
        print(f"Bank balance = {bank_balance}")
    else:
        print("Enter valid pin")

elif operation == "mini statement":
    if len(mini_statement) == 0:
        print("No transactions yet")
    else:
        print(f"Mini statement : {mini_statement}")

else:  # change pin
    old_pin = int(input("Enter old pin : "))
    if old_pin != security_pin:
        print("Invalid old pin---")
    else:
        new_pin = int(input("Enter new pin : "))
        if new_pin == old_pin:
            print("New pin must be different from old pin")
        elif new_pin < 1000 or new_pin > 9999:
            print("Pin must be a 4-digit number")
        else:
            security_pin = new_pin
            print("Pin reset is successful")