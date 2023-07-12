from calculator_art import logo


#calculator

#Add
def add(n1,n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2


#Divide
def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  """
  This function take an input of calculate its with the user operation choice
  """
  print(logo)
  num1 = float(input("What is the first number?: "))
  # looping through the operations dictionary
  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:
    operators_symbol = input("pick one operation from the above: ")
    num2 = float(input("What is the next number?: "))
    operators = operations[operators_symbol]
    answer = operators(num1, num2)
    print(f"{num1} {operators_symbol} {num2} = {answer}")
    
    repeat = input(f"Type 'y' to continue calculating with {answer}, or type 'no' to start a new calculation: ")
    if repeat == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()


calculator()
      



    

