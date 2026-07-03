def calculator():
    print('=== Calculator ===')
    print('Available operations: +, -, *, /')
    
    num1 = float(input('Enter the first number: '))
    operation = input('Enter the operation (+, -, *, /): ')
    num2 = float(input('Enter the second number: '))
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print('Error: cannot divide by zero.')
            return
        result = num1 / num2
    else:
        print('Invalid operation.')
        return
    print(f'Result: {result}')

calculator()
