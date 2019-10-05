def add(x, y):
   return (x + y)
def subtract(x, y):
   return (x - y)

def multiply(x, y):
   return (x * y)

def divide(x, y):
   return (x / y)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The sum of x and y is: ",add(num1,num2))
print("The product of x and y is: ",multiply(num1,num2))
print("The quotient of x and y is: ",divide(num1,num2))
print("The difference of x and y is: ",subtract(num1,num2))
