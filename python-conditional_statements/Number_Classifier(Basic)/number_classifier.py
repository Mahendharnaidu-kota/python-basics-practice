#Number classifier
num = int(input("Enter a whole number : "))

if num > 0:
    sign = "Positive"
elif num < 0:
    sign = "Negative"
else:
    sign = "Zero"

if num % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"

if num % 10 == 0:
    divisibility = "Divisible by both 5 and 10"
elif num % 5 == 0:
    divisibility = "Divisible by 5"
else:
    divisibility = "Num not divisible by 5 or 10"

print("-" * 40)
print("******* number classifier ********")
print(f"input num is {num}")
print(f"num is {sign}")
print(f"num is {parity}")
print(f"num is {divisibility}")

print("*" * 40)