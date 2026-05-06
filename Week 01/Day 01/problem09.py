# Program 09: Ask user for Principal(P), Time(T) and Rate(R)
# Convert them to float and compute Simple interest

principal = input("Enter the principal amount: ")
time = input("Enter the time or duration in years: ")
rate = input("Enter the rate of interest: ")

principal = float(principal)
time = float(time)
rate = float(rate)

simple_interest = (principal * time * rate) / 100

print("The Simple interest is ", simple_interest)