# In this task, people can choose either investment or bond
# If choosing investment, enter The amount of money that you would like to deposit, interest rate and number of year
# choosing simple or compound
# calculate in different equation

# if choosing bond
# enter present value, annual interest rate and number of month
# calculate

# The maths below can be calculated. However, how can I write the code that if the user type "INVESTMENT", the code still can be run
# Please advise

print("investment - to calculate the amount of interest you'll learn earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print("enter either:'investment or bond' form the menu above to proceed")

# user enter investment or bond
user_option = input(" What is your choice ? ")

# If user choosing investment
if user_option.lower() == "investment":
    P = int(input(" The amount of money that you would like to deposit:"))
    print(P)
    r = int(input(" The interest rate%: "))  # r should be divided by 100
    R = r / 100
    t = int(input(" Number of years:"))
    print(t)
    "1" == int(1)
    print(int("1"))
    kind_of_interest = input(" simple or compound: ")
    A = print("Total amount once the interest has been applied is")
    if kind_of_interest.lower() == "simple":
        A = print(float(P * (1 + R * t)))
    elif kind_of_interest.lower() == "compound":
        A = print(float(P * (1 + R) ** t))

elif user_option.lower() == "bond":
    P = int(input("Present value of the house"))
    i = int(input("annual interest rate")) / 100 / 12
    n = int(input("number of months over which the bond will be repaid"))
    A = "The repayment of a month is"
    A = print(float(i * P) / (1 - (1 + i) ** (-n)))

