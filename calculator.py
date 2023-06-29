print("Calculator")
result = 0
run_again = True

def calculate(operation: str, num1: int, num2: int):
    # global keyword allows us to modify the variable outside of the current scope
    global result
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "/":
        if num2 == 0:
            print("Division by zero is undefined. Enter a non-zero number.")
            return
        else:
            result = num1 / num2
    elif operation == "x":
        result = num1 * num2
    print("Result:", result)

 # this can be while True. Thought changing the value of run_again to false would
 # cause the session to end   
while run_again:
    operations = ["+", "-", "/", "x"]
    operation = input("Pick an operation: +, -, /, x")
    if operation in operations:
        try:
            num1 = int(input("Enter num 1: "))
            num2 = int(input("Enter num 2: "))
            calculate(operation, num1, num2)
            continue_calc = str(input("Continue? y/n"))
            if continue_calc == "n":
                break
        # ValueError - raised when operation or fn receives an arg that has the right type but an innapropriate value        
        except ValueError:
            print("Invalid input. Please try again")
    else:
        print("Invalid input, try again please")
    



   







