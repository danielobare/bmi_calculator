print ("""You now have the opportunity to calculate your BMI using this custom made calculator.
This program was created by Daniel Obare.

BMI is short for Body Mass Index.

The formula for calculating BMI is given by: weight/(height)^2""")

while True:
    try:
        weight=float(input("Please enter your approximate weight in kilograms(kg) example 58 or 62.55 or 77.1: "))
        break
    except ValueError:
        print("Please enter an integer value only...")
        continue

while True:
    try:
        height=float(input("Please enter your approximate height in meters(m) example 1.76 or 1.5: "))
        break
    except ValueError:
        print("Please enter your accurate height...")
        continue


BMI_ur=(int(weight)/(float(height)*float(height)))
BMI=round(BMI_ur)
print("Your BMI is: ", BMI )

if (BMI<18.5):
    print("Underweight.")
elif (18.5 >= BMI <= 24.9):
    print("Normal weight.")
elif (25 >= BMI <= 29.9):
    print("Overweight.")
else:
    print("Obesity.")


    