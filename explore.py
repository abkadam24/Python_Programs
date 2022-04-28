#to get power values
import random

power = 5**2
print(power)

z = 1j      #complex data type
print(type(z))

print('C:\Abhi\name')  #\n is for new line
print(r'C:\Abhi\name')  # if we use 'r' at be beginning it will print whole in one line

Str = 3*'ab'+'cd'   #concating 3 times ab with cd
print(Str)
print('py' 'thon')  #can be directly concatinate

squares = [1, 4, 9, 17, 25]
print(squares)
squares[3] = 16     #we can also replace value using array of that number
print(squares)
squares.append(6**2)    #We can use append method for adding items at end
squares.append(7**2)
print(squares)

j= ['a','b','c']
k= [1,2,3]
x=[j,k]     #to nest lists
print(x)
print(x[0])
print(x[0][1])

x= 5.5
x= int(x)     #converting float into int
print(x)

print(random.randrange(1, 10))     #to import random number between 1 to 10





