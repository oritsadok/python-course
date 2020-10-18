
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

c = a
a = b
b = c

print(a)
print(b)

#####

x = int(input('Enter value for x: '))
y = int(input('Enter value for y: '))
# create a temporary variable and swap the values
temp = x
x = y
y = temp
# Print the result
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))