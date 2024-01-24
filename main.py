#Define four subroutines - add, subtract, multiply, divide that add multiply etc two numbers and return the result. Each should have two integer number arguments.

def add(number1, number2):
  return number1 + number2
  

def subtract(number1, number2):
  return number1 - number2
  

def multiply(number1, number2):
  return number1 * number2


def divide(number1, number2):
  return number1 / number2



#The user is asked to input two numbers.  These numbers will be passed as arguments into one of the subroutines.
#The user is asked to input 1 to add, 2 to subtract etc.
#If they input 1, call the ‘add’ subroutine, input 2 calls the ‘subtract’ subroutine etc
#Output the returned result as part of a sentence.


calculator = int(input("Press 1 to add: Press 2 to subtract: Press 3 to multiply: Press 4 to divide"))

if calculator == 1:
  num1 = int(input("Enter a number to add"))
  num2 = int(input("Enter a second number to add"))
  outputsum = (add(num1, num2))
  print(str(outputsum) + " is your answer.")

elif calculator == 2:
  num1 = int(input("Enter a number to subtract"))
  num2 = int(input("Enter a second number to subtract"))
  outputsubstitution = (subtract(num1, num2))
  print(str(outputsubstitution) + " is your answer.")
elif calculator == 3:
  num1 = int(input("Enter a number to multiply"))
  num2 = int(input("Enter a second number to multiply"))
  outputmultiplication= (multiply(num1, num2))
  print(str(outputmultiplication) + " is your answer.")
elif calculator == 4:
  num1 = int(input("Enter a number to divide"))
  num2 = int(input("Enter a second number to divide"))
  outputdivide = (divide(num1, num2))
  print(str(outputdivide) + " is your answer")
else:
  print("Error: Please enter a calculator mode which is a number from 1-4")
