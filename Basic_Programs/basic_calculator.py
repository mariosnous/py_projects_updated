

def add(a, b):
    addition_result = a + b

    print(f"The result is : {addition_result}")


def sub(a, b):

    subtraction_result = a - b

    print(f"The result is : {subtraction_result}")


def multiplication(a, b):

    multi_result = a * b
    print(f"The result is : {multi_result}")


def division(a, b):

    division_result = a / b
    print(f"The result is : {division_result}")


while True:

    print("Please choose one of these options :\n A: Addition\n S: Subtraction\n M: Multiplication \n D: Division")

    choice = input(
        "Please choose your math operation or press 'q' to quit ? : ")

    if choice == 'a' or choice == 'A':
        print("You chose addition")
        a = int(input("first number : "))
        b = int(input("Second number : "))
        add(a, b)
    elif choice == 's' or choice == 'S':
        print("You chose subtraction")
        a = int(input("first number : "))
        b = int(input("Second number : "))
        sub(a, b)
    elif choice == 'm' or choice == 'M':
        print("You chose multiplication")
        a = int(input("first number : "))
        b = int(input("Second number : "))
        multiplication(a, b)
    elif choice == 'd' or choice == 'D':
        print('You chose division')
        a = int(input("first number : "))
        b = int(input("Second number : "))
        division(a, b)
    elif choice == 'q' or choice == 'Q':
        print("Program is closed ")
        break
