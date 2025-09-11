import math

a :float = float(input('Enter a number: '))

def square(a):
    return math.sqrt(a)

def log(a):
    return math.log(a, 10)

def sinValue(a):
    return math.sin(a)

print('Square root of ', a , 'is: ', square(a))
print('Logarithm of ', a , 'is: ', log(a))
print('Sine of ', a , 'is: ', sinValue(a))
