#!/usr/bin/python
# Program make a simple calculator that can add, subtract, multiply and divide using functions

# define functions
def add(x,y): return x + y

def subtract(x,y): return x - y

def multiply(x,y): return x * y

def divide(x,y): return x / y

def factorial(x,y): return x ** y 

# take input from the user
#print("Select operation.")
#print("1.Add")
#print("2.Subtract")
#print("3.Multiply")
#print("4.Divide")

choice = int(input("Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n"))
if choice not in [1,2,3,4]:
	print('Invalid input dumbass!')
	exit()

a = int(input("first number: "))
b = int(input("second number: "))

if choice == 1:
   print '{} + {} = {}'.format(a, b, add(a,b))

elif choice == 2:
   print '{} - {} = {}'.format(a, b, subtract(a,b))

elif choice == 3:
   print '{} * {} = {}'.format(a, b, multiply(a,b))

elif choice == 4:
   print '{} / {} = {}'.format(a, b, divide(a,b))
else:
   print("Invalid input")




