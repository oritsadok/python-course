'''
x = int(input('Enter a number between 100 - 999'))

dsum = x%10
x //= 10
dsum += x%10
x //= 10
dsum+= x
print(dsum)
'''

#######

avg = 90
knows_py = True
knows_c = False
#res = avg >=85 and (knows_py == True or knows_c == True)
res = avg >= 85 and (knows_py or knows_c)
print(res)

#####
pi = 3.14159265359
print('the value of pi is:' + str(pi))
####
print('The value of {} is {}'.format('pi', 3.14159265359))
###
print('The value of {} is {:.2f}'.format('pi', 3.14159265359))
####
print('The value of {0} is {1}'.format('pi', 3.1415))
###
print('The value of {1} is {0}'.format('pi', 3.1415))
#######

number = int(input("Enter a number: "))
even = number%2
print("The parity of {} is {}".format(number, even))

units = number%10
small_number= number//10
tens = small_number%10

print("The units and tens of {} are {} and {} respectively".format(number, units, tens))
