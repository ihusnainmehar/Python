#This is simple BMI Calculator
name = input("Enter your name: ")
Weight = int(input("Enter Your Weight(kg): "))
Height = int(input("Enter Your Height(cm): "))
Height_m = Height/100
BMI = Weight/(Height_m**2)
if BMI < 18.5:
    category = "Underweight"
elif BMI < 25:
    category = "Normal"
elif BMI < 30:
    category = "Overweight"
else:
    category = "Obese"


print("\n========== BMI Report ==========")
print(f"Name: {name}")
print(f"Weight: {Weight} kg")
print(f"Height: {Height} cm")
print(f"BMI: {BMI:.2f}")
print(f"Category: {category}")