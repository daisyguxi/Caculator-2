"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
"""repeat forever 
read input
tokenized input
    if first token is 'q':
        quit
    else:
        decide with math function to call
        if first token is 'pow':
            call the power function with other two tokens TESTING A CHANGE"""
    
while True:
    user_input = input("What is your equation? ")
    token_input = user_input.split(' ')
    token = token_input[0] 
   

    if 'q' in token_input:
      print("Good bye!")
      break

    num1 = float(token_input[1])

    if len(token_input) < 3:
        num2 = '0'
    else:
        num2 = float(token_input[2])

    if token == '+':
        equation = add(num1, num2)
    elif token == '-':
         equation = subtract(num1, num2)
    elif token == '*':
        equation = multiply(num1, num2)
    elif token == '/':
         equation = divide(num1, num2)
    elif token == '**':
        equation = square(num1)
    elif token == '***':
         equation = cube(num1)
    elif token == 'pow':
        equation = power(num1, num2)
    elif token == '%':
         equation = mod(num1, num2)
    else:
       print("Please enter equation.")
    print(equation)
    
