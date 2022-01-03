import art
print(art.logo)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

operations = {
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply
}

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for operation in operations:
    print(operation)

operation_symbol = input("Pick an operation from the list above: ")

answer = operations[operation_symbol](a,b)

print(f'{a} {operation_symbol} {b} = {answer}')
