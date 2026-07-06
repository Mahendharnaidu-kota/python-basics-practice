#BMI Calculator (no conditionals, functions , or loops)

weight = float(input("Enter weight in kgs : "))
height = float(input("Enter height in mtrs : "))

bmi = weight / (height * height)

index = (bmi >= 18.5) + (bmi >= 25) + (bmi >= 30)

categories = ["Underweight", "Normal", "Overweight", "Obese"]
category = categories[index]

print("BMI Calculator")
print("---------------------")
print(f"BMI      : {bmi:.2f} kg/m^2")
print(f"Category  : {category}")