height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
w=float(weight)
h=float(height)
BMI =(w/(h*h))   #BMI= w/(h**2)
print(BMI)
if BMI <18.5:
  print("Underweight")
elif BMI<25:
  print("Normal weight")
elif BMI < 30:
  print("Slightly over weight")
elif BMI < 35:
  print("Obese")
else:
  print("Clinically obese")
