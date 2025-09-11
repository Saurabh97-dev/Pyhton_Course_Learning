
a : int = int(input('Enter a number '))
def factorialFunction(a):
    if a < 2 :
        return 1
    else:
        return a * (factorialFunction(a-1))

result = factorialFunction(a)
print('Factorial of',a ,'is: ',result)

