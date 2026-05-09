# take salary input
# calculate final tax rate

salary = int(input("Enter your salary: "))

if salary <= 30000:
    tax_rate = 5

elif salary <= 70000:
    tax_rate = 15

else:
    tax_rate = 25

tax = salary * tax_rate / 100
in_hand = salary - tax

print("Tax =", tax)
print("In-hand amount =", in_hand)