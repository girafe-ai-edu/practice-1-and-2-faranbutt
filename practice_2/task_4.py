# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
total = 0
while True: 
    number = input('Enter a 4-digit number: ')
    if len(number) != 4:
        print('Please enter a 4-digit number')
    else:
        break

for num in number:
    total += int(num)
print(f'The sum of the digits is {total}')