height = float(input("Enter height: "))
weight = float(input("Enter weight: "))


def BMI(height, weight):
    bmi = weight/(height**2)*10000

    if bmi < 16:
        return 'severely underweight', bmi

    elif bmi >= 16 and bmi < 18.5:
        return 'underweight', bmi

    elif bmi >= 18.5 and bmi < 25:
        return 'healthy', bmi

    elif bmi >= 25 and bmi < 30:
        return 'overweight', bmi

    elif bmi >= 30:
        return 'obese', bmi


quote, bmi = BMI(height, weight)
print('Your BMI is: {} and you are: {}'.format(bmi, quote))
