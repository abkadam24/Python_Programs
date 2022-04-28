kilometers = float(input("Enter value in kilometers: "))    #'input' is to take value from user
conv_value = 0.621371
miles = kilometers * conv_value
print('in miles:', (miles))

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))