# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in meters: '))


#code here
BMI = weight/(height**2)
print(f'Your BMI is {BMI:.2f}')

if BMI < 18.5:
    print('Underweight')
elif BMI >= 18.5 and BMI < 25:
    print('Normal weight')
elif BMI >= 25 and BMI < 30:
    print('Overweight')
else:
    print('Obesity')

