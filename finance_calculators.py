import math 

def calculator():

    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay on a home loan \n\n")

    # The user must choose between investment and bond
    # Depending on the choice made, a series of questions will be asked in order to generate an answer
    # If the answer to any question isn't whats expected then a ValueError message is defined
    # The user is then taken back to the question to try again
    # The loops continue until acceptable answers are inputed

    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    if choice == "investment":
        while True:
            try:
                deposit = float(input("How much money are you depositing (£)? "))
                break
            except ValueError:
                print("Please enter a valid amount, do not include the '£' sign.")

        # Only numbers allowed - decimals are accepted
        while True:
            try:
                interest_rate = float(input("At what interest rate (%) "))
                break
            except ValueError:
                print("Please enter the value of the interest rate, do not include the '%' sign.")

        # The user can only enter a whole number, anything else raises an error
        while True:
            try:
                term = int(input("What is the length of your investment, in years? "))
                break
            except ValueError:
                print("Please enter a valid investment term, numbers only rounded to the nearest whole number.")

        # In this loop we ensure that no other input is excepted other than simple and compound
        # If something else is entered a ValueError is raised and the user is promted to make a new entry
        while True:
            try:
                type = input("Please specify if you want 'simple' or 'compound' interest by entering either 'simple' or 'compound': ").lower()
                if type != "simple" and type != "compound":
                    raise ValueError
                break
            except ValueError:
                print("Please ensure you have only selected either 'simple' or 'compound'")

        # Once all the inputs have been raised we calculate the investment return depending on which type has been selected
        if type == "simple":
            investment_interest = deposit * (1 + ((interest_rate/100) * term))
            print(f"The total interest earned on this investment is £{investment_interest:.2f}")

        elif type == "compound":
            investment_interest = deposit * math.pow((1 + (interest_rate/100)), term)
            print(f"The total interest earned on this investment is £{investment_interest:.2f}")

    elif choice == "bond":
        while True:
            try:
                present_value = int(input("What is the present value of the house (£)? "))
                break
            except ValueError:
                print("Please enter a valid present value, do not include the '%' sign.")

        while True:
            try:
                rate_of_interest = int(input("What is the rate of interest (%)? "))
                # Here im taking the interest rate entered by the user and dividing it by 100 then by 12
                # this is so it is in the format we need for the bond formula
                rate_of_interest_i = (rate_of_interest / 100) / 12
                break
            except ValueError:
                print("Please enter a valid interest rate.")

        while True:
            try:
                months = int(input("How many months will it take to repay the bond? "))
                break
            except ValueError:
                print("Please enter a valid loan term.")

        # Here we use the above to calculate the bond repayment using the bond formula
        repayment = (rate_of_interest_i * present_value) / (1 - (1 + rate_of_interest_i)**(-months))
        print(f"This is how much money you will have to repay on your bond each month: {repayment:.2f}")

    else:
        print("You didn't select a valid response.")
    
    # If the user doesnt select a valid response to choice, they are prompted to try the calculator again
    # The function will then repeat itself so that they can enter a correct option

    repeat = input("Would you like to try again? ").lower()
    if repeat == "yes":
        calculator()
    else:
        print("Thank you for using this calculator.")

    # otherwise the code stops.

calculator()
