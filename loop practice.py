# 5.1 Programming Assignment: Loops
# DSC 510
# Rosie Navarro
# 04/14/26


def calculate_average():
    user_numbers = int(input("How many numbers do you want?"))
    total = 0

    for user in range(user_numbers):
        num = int(input("Enter a number:"))
        total += num

    average = total / user_numbers
    return average



def perform_calculation():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    operator = input("Choose one of the following: +,-,/,*:")
    if operator == "+":
        calculation = num1 + num2
    elif operator == "-":
        calculation = num1 - num2
    elif operator == "/":
        calculation = num1 / num2
    elif operator == "*":
        calculation = num1 * num2
    else:
        print("Invalid please enter one of the operators")
        return None
    return calculation



def main():
    while True:
        print("user please select one of the following:")
        print(" 1: perform a calculation, 2: calculate average, 3: exit program")

        user_decides = input("Choose option 1, 2, or 3:")

        if user_decides == "1":
            result = perform_calculation()
            print("Calculation result = ", result)

        elif user_decides == "2":
            result = calculate_average()
            print("Average = ", result)

        elif user_decides == "3":
            print("you are now exiting the program")
            break

        else:
            print("Invalid please enter one of the options")


if __name__ == "__main__":
    main()