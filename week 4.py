# 4.1 programming assignment- Functions
# DSC510
# Rosie Navarro
# 04/09/26

def cost_calculation(feet, cost_per_foot):
    """
    Calculates the total cost, multiplying number of feet by the prices per foot

    Parameters
    -------------
    feet: float
        the number of feet of fiber optics cable
    cost_per_foot: float
        the cost per foot of cable.

    Returns
    ---------
    float
        Calculated cost (total cost)
    """
    return feet * cost_per_foot


def main():
    print('Hello user! The following is more information for Fiber Optics.')
    """
    Main function that runs the calculation.
    Collects the user inputs for feet and company.
    Once there is something for user input, pricing is determined, total cost is calculated, and makes a receipt.
    """
    # Following is error handling
    # continue used for loop if there is still an invalid output
    #break once valid it continues on
    while True:
        try:
            feet = float(input("Enter number of feet:"))
            if feet < 0:
                print ("Please Enter a positive number")
                continue
            break
        except ValueError:
            print("Invalid input")

    # Following is user inputs
    company = input("Enter Company Name:")

    # Cost per foot for varying number of feet
    if feet > 500:
        cost_per_foot = .55
    elif feet > 250:
        cost_per_foot = .75
    elif feet > 100:
        cost_per_foot = .85
    else:
        cost_per_foot = .95

    # total cost calculation using function
    total_cost = cost_calculation(feet, cost_per_foot)

    # Following is receipt for the customer: displays company name, cost per foot, and total cost
    print("Receipt:")
    print("Company Name:", company)
    print(f"Cost per foot: ${cost_per_foot: .2f}")
    print(f"Total Cost: ${total_cost: .2f}")


if __name__ == "__main__":
    main()