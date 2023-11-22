def calcule(num1, operator, num2):
    print('number: num1 ')
    print('operator:  operator ')
    print('second number: num2 ')
    if operator == '*':
        return num1*num2
    elif operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2
    elif operator == '/':
        return num1/num2 

print(calcule(4, '-', 5))