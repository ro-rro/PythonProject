# 5.1 Programming Assignment: Loops
# DSC 510
# Rosie Navarro
# 04/14/26



def calculate_average():

    """
    Asks user to enter a specified number of values (user_numbers).
    calculates the average of the values using a loop.

    Returns:
        float: average of the numbers entered by the user.
    """

    # user input of the number of numbers they want ot use. EX: if they choose 10 they will enter 10 numbers.
    try:
        user_numbers = int(input("How many numbers do you want to use?"))
    except ValueError:
        print("Please enter a number.")
        return None

    total = 0

    # this part shows user input of the numbers they want to use in average.
    for user in range(user_numbers):
        try:
            num = int(input("Enter a number:"))
        except ValueError:
            print("Invalid. Please enter a number. ")
            return None
        total += num

    # Average calculation
    average = total / user_numbers
    return average



def perform_calculation(operation):
    """
    user input of two values (float) and their choice of operator (-, +, *, /).
    a specific math calculation is then performed.

    parameter:
        String: operation (-, +, /, *)

    Returns:
        float: results from user calculation, or none if there is an invalid entry.
    """

    try:
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
    except ValueError:
        print("Invalid. Please enter a number")
        return None


    if operation == "+":
        calculation = num1 + num2
    elif operation == "-":
        calculation = num1 - num2
    elif operation == "/":
        calculation = num1 / num2
    elif operation == "*":
        calculation = num1 * num2
    else:
        print("Invalid please enter one of the operators")
        return None

    return calculation



def main():

    """
    controls the program, acts like a menu allowing the user to choose between performing a
    calculation (performing_calculation), calculating an average (calculate_average),
    or leaving the program. It runs continuously until the user decides to leave.
    """

    while True:
        print("User please select one of the following:")
        print(" 1: perform a simple math calculation, 2: calculate average, 3: exit program")


        user_decides = input("Choose option 1, 2, or 3:")


        if user_decides == "1":
            operation = input("choose one of the following: +, -, /, * ")
            result = perform_calculation(operation)
            print("Calculation result = ", result)

        elif user_decides == "2":
            result = calculate_average()
            print("Average = ", result)

        elif user_decides == "3":
            print("You are now exiting the program")
            break

        else:
            print("Invalid please enter one of the options")


if __name__ == "__main__":
    main()
