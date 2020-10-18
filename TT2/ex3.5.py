
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

y = x + y
x = y - x
y = x - y

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

#####
# the elegant way
x = 1
y = 2
x, y = y, x
print(x,y)