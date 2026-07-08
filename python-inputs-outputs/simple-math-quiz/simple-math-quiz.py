# Simple Math Quiz

print("Question 1: What is 5 + 2?")
ans1 = float(input("Enter answer 1: "))
is_correct1 = (ans1 == 7)
feedback1 = ["Try again!", "Great job!"][is_correct1]
print(feedback1)
print("-" * 40)

print("Question 2: What is 4 divided by 2?")
ans2 = float(input("Enter answer 2: "))
is_correct2 = (ans2 == 2)
feedback2 = ["Try again!", "Great job!"][is_correct2]
print(feedback2)
print("-" * 40)

print("Question 3: What is 10 squared (10^2)?")
ans3 = float(input("Enter answer 3: "))
is_correct3 = (ans3 == 100)
feedback3 = ["Try again!", "Great job!"][is_correct3]
print(feedback3)
print("-" * 40)

score = is_correct1 + is_correct2 + is_correct3
total = 3
percentage = (score / total) * 100

print(f"You got {score}/{total} correct ({percentage:.2f}%)")