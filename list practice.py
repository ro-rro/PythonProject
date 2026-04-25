def main():
    temperature = []

    while True:
        user_input = input("Please enter a temperature or 'done' to exit: ")
        if user_input == "done":
            break

        try:
            temp = float(user_input)
            if temp < -100 or temp > 130:
                print("please enter a realistic temperature")
            else:
                temperature.append(temp)

        except ValueError:
            print("Please enter a number.")

    if temperature:
        print("This is the min temperature recorded: ",min(temperature))
        print("This is the max temperature recorded: ", max(temperature))
        print("This is the number of temperatures entered: ", len(temperature))
    else:
        print("No valid entries were entered.")

if __name__ == "__main__":
    main()