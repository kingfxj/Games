# Exercise 1.1
def calculator_1():
    print("Welcome to CSW Simple Calculator")

    number_1 = float(input("Please enter your first number: "))
    number_2 = float(input("Please enter your second number: "))

    print(str(number_1) + ' + ' + str(number_2) + ' is ' + str(number_1 + number_2))


# Exercise 1.2
def calculator_2():
    print("Welcome to CSW Simple Calculator")

    print('Please choose an operator from the following list')
    operator = input("[+, -, *, /, **, //, %, ==, !=, >, <, >=, <=]: ")
    number_1 = float(input("Please enter your first number: "))
    number_2 = float(input("Please enter your second number: "))

    if operator == '+':
        print(str(number_1) + ' + ' + str(number_2) + ' is ' + str(number_1 + number_2))
    elif operator == '-':
        print(str(number_1) + ' - ' + str(number_2) + ' is ' + str(number_1 - number_2))
    elif operator == '*':
        print(str(number_1) + ' * ' + str(number_2) + ' is ' + str(number_1 * number_2))
    elif operator == '/':
        print(str(number_1) + ' / ' + str(number_2) + ' is ' + str(number_1 / number_2))
    elif operator == '**':
        print(str(number_1) + ' ** ' + str(number_2) + ' is ' + str(number_1 ** number_2))
    elif operator == '//':
        print(str(number_1) + ' // ' + str(number_2) + ' is ' + str(number_1 // number_2))
    elif operator == '%':
        print(str(number_1) + ' % ' + str(number_2) + ' is ' + str(number_1 % number_2))
    elif operator == '==':
        print(str(number_1) + ' == ' + str(number_2) + ' is ' + str(number_1 == number_2))
    elif operator == '!=':
        print(str(number_1) + ' != ' + str(number_2) + ' is ' + str(number_1 != number_2))
    elif operator == '>':
        print(str(number_1) + ' > ' + str(number_2) + ' is ' + str(number_1 > number_2))
    elif operator == '<':
        print(str(number_1) + ' < ' + str(number_2) + ' is ' + str(number_1 < number_2))
    elif operator == '>=':
        print(str(number_1) + ' >= ' + str(number_2) + ' is ' + str(number_1 >= number_2))
    elif operator == '<=':
        print(str(number_1) + ' <= ' + str(number_2) + ' is ' + str(number_1 <= number_2))
    else:
        print('Invalid operator')


# Exercise 2
def smallestNumber():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Please enter an integer: ")))
    print(numbers)

    smallest = numbers[0]
    for i in range(1, 5):
        if numbers[i] < smallest:
            smallest = numbers[i]

    print(smallest)


# Exercise 1.3
def calculator_3():
    print("Welcome to CSW Simple Calculator")

    while True:
        print('Please choose an operator from the following list')
        operator = input("[+, -, *, /, **, //, %, ==, !=, >, <, >=, <=]: ")
        number_1 = float(input("Please enter your first number: "))
        number_2 = float(input("Please enter your second number: "))

        if operator == '+':
            print(str(number_1) + ' + ' + str(number_2) + ' is ' + str(number_1 + number_2))
        elif operator == '-':
            print(str(number_1) + ' - ' + str(number_2) + ' is ' + str(number_1 - number_2))
        elif operator == '*':
            print(str(number_1) + ' * ' + str(number_2) + ' is ' + str(number_1 * number_2))
        elif operator == '/':
            print(str(number_1) + ' / ' + str(number_2) + ' is ' + str(number_1 / number_2))
        elif operator == '**':
            print(str(number_1) + ' ** ' + str(number_2) + ' is ' + str(number_1 ** number_2))
        elif operator == '//':
            print(str(number_1) + ' // ' + str(number_2) + ' is ' + str(number_1 // number_2))
        elif operator == '%':
            print(str(number_1) + ' % ' + str(number_2) + ' is ' + str(number_1 % number_2))
        elif operator == '==':
            print(str(number_1) + ' == ' + str(number_2) + ' is ' + str(number_1 == number_2))
        elif operator == '!=':
            print(str(number_1) + ' != ' + str(number_2) + ' is ' + str(number_1 != number_2))
        elif operator == '>':
            print(str(number_1) + ' > ' + str(number_2) + ' is ' + str(number_1 > number_2))
        elif operator == '<':
            print(str(number_1) + ' < ' + str(number_2) + ' is ' + str(number_1 < number_2))
        elif operator == '>=':
            print(str(number_1) + ' >= ' + str(number_2) + ' is ' + str(number_1 >= number_2))
        elif operator == '<=':
            print(str(number_1) + ' <= ' + str(number_2) + ' is ' + str(number_1 <= number_2))
        else:
            print('Invalid operator')

        user = ''
        while user.upper() not in ['Y', 'N', 'YES', 'NO']:
            user = input("Do you want to do another calculation? Y/N ")
        if user.upper() in ['N', 'NO']:
            break

    print('Thank you for using Simple Calculator')


if __name__ == '__main__':
    # calculator_1()
    # calculator_2()
    # smallestNumber()
    calculator_3()
