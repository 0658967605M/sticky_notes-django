import math 

# To proceed with the calculation choose the type of investment or bond
investment_or_bond = input("Choose either 'investment' or 'bond' from the menu above: ")
if investment_or_bond != "investment" and investment_or_bond != "bond":
    if investment_or_bond != "Investment" and investment_or_bond != "Bond":
        if investment_or_bond != "INVESTMENT" and investment_or_bond != "BOND":
            print("[Invalid input. Please enter 'investment' or 'bond'.]")

# If the user selects "Investment" , ask the user to input the amount they want to deposit
if investment_or_bond == "investment" or investment_or_bond == "Investment" or investment_or_bond == "INVESTMENT":
    investment_amount = float(input("Enter the amount you want to invest: "))
    print(f"You have chosen to invest: {investment_amount}")

# Ask the user to enter the interest rate for the investment
    investment_rate = float(input("Enter the annual interest rate (as a percentage): "))
    print(f"The annual interest rate for your investment is: {investment_rate}%")

# Ask the user to enter the number of years they plan to invest
    investment_years = int(input("Enter the number of years you plan to invest: "))
    print(f"You plan to invest for: {investment_years} years") 

    # Ask the user to enter "simple" or "compound" interest , and store in a variable
    investment_type = input("Enter 'simple' for Simple Interest or 'compound' for Compound Interest: ").lower()
    if investment_type == "simple":
        print(f"[Simple interest = {investment_amount * ( 1 + investment_rate / 100 * investment_years)}]")
    elif investment_type == "compound":
        print(f"[Compound interest = {investment_amount * math.pow((1 + investment_rate / 100), investment_years)}]")
    else:
        print("[Invalid input for interest type. Please enter 'simple' or 'compound'].")

# If the user selects "Bond", Ask the user to enter the present value of the house
if investment_or_bond == "bond" or investment_or_bond == "Bond" or investment_or_bond == "BOND":
    house_value = float(input("Enter the present value of the house: "))
    print(f"The present value of the house is: {house_value}")

# Ask the user to enter the interest rate for the bond
    bond_rate = float(input("Enter the annual interest rate for the bond (as a percentage): "))
    print(f"The annual interest rate for your bond is: {bond_rate}%")

# Ask the user to enter the number of months they plan to take to pay the bond
    bond_months = int(input("Enter the number of months you plan to take to pay the bond: "))
    print(f"You plan to take {bond_months} months to pay the bond.")
    print(f"Monthly repayment = {(bond_rate / 100 / 12 * house_value) / (1 - (1 + bond_rate / 100 / 12) ** (-bond_months))}")