height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kgs? "))
bmi = round(weight/(height**2))
if bmi < 18.5:
    print(f"Underweight {bmi}")
elif bmi < 25:
    print(f"Normal weight {bmi}")
elif bmi < 30:
    print(f"Overweight {bmi}")
elif bmi < 35:
    print(f"Obese {bmi}")
else:
    print(f"Clinically obese {bmi}")
