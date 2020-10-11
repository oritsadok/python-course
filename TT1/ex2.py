import math

#ex2
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))

print(num1+num2)
print(num1*num2)


###############

# This program adds two numbers

num1, num2 = input("Enter two numbers separated by a single space: ").split(' ') # '1 2'

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

# Add two numbers
prod = float(num1) * float(num2)

# Display the product
print('The product of {0} and {1} is {2}'.format(num1, num2, prod))