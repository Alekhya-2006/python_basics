# divisible by 5 and 11

n = int(input("Enter a number: "))

if(n % 5 == 0 and n % 11 == 0):
    print(f'{n} is divisible by both 5 and 11')
elif(n % 5 == 0 or n % 11 == 0):
    if(n % 5 != 0):
        print(f'{n} is divisible by 11 but not 5')
    else:
        print(f'{n} is divisible by 5 but not 11')
else:
    print(f'{n} is not divisible by both 5 and 11')                