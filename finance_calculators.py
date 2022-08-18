import math

#This is the first set of ouputs that will occur when the program starts
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("")
print("investment   - to calculate the amount of interest uou'll earn on interest")
print("bond         - to calculate the amount you'll have to pay on home loan")
print("")
calculation_type = input("Enter the calculation you would like to do: ")

if calculation_type.lower() == "investment":
    deposit_amount = float(input("Enter the amount of money that you are going to deposit: "))
    interest_rate = float(input("Enter the interest rate: "))
    years = float(input("Enter the amount of years you plan to invest for: "))
    interest = input("Do u want a simple or compound interest: ")
    if interest == "simple":
        total_amount = deposit_amount * (1 + (interest_rate/100) * years)
        print("{} was gained in {} years with {}'%' interset rate".format(total_amount, years, interest_rate))
    elif interest == "compound":
        total_amount = deposit_amount * math.pow((1+(interest_rate/100)), years)
        print("{} was gained in {} years with {}'%' interset rate".format(total_amount, years, interest_rate))

elif calculation_type.lower() == "bond":
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the monthly interest rate: "))
    months = float(input("Enter the amount of months in which u want to pay the bond: "))
    repayment = ((interest_rate/12)*present_value)/(1 - (1+(interest_rate/12))**(-months))
    print("{} will have to be repaid each month".format(repayment))

else:
    print("This is not one of the options provided to you.")
    print("Investment and bond is the only options to choose from")
