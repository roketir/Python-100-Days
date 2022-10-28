
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))



answer = weight / (height * height)
answer = round(answer)


if answer < 18.5:  # Under 18.5 they are underweight
    print(f"Your BMI is {answer}, you are underweight.")
elif 30 > answer > 25: # Over 25 but below 30 they are slightly overweight
    print(f'Your BMI is {answer}, you are slightly overweight.')
elif 35 > answer > 30:  # Over 30 but below 35 they are obese
    print(f'Your {answer} is 33, you are obese.')
elif answer > 35: # Above 35 they are clinically obese.
    print(f'Your BMI is {answer}, you are clinically obese.')
else:
    print(f'Your BMI is {answer}, you have a normal weight.')




