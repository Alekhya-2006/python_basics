# Count even or odd numbers

nums = []


def even_odd(lst):

    even = 0
    odd = 0

    for i in lst:

        if i % 2 == 0:
            even += 1

        else:
            odd += 1

    return even, odd


while True:

    print("\n1. Add Element")
    print("2. View List")
    print("3. Count Even/Odd")
    print("4. Exit")

    n = int(input("Choose 1 - 4: "))

    if n == 1:

        num = int(input("Enter the number you want to add: "))
        nums.append(num)

        print("Number added successfully")

    elif n == 2:

        if len(nums) == 0:
            print("List is empty")

        else:
            print("Current List:", nums)

    elif n == 3:

        if len(nums) == 0:
            print("List is empty")

        else:

            even, odd = even_odd(nums)

            print(f"Even: {even}")
            print(f"Odd: {odd}")

    elif n == 4:

        print("Program exited successfully")
        break

    else:
        print("Invalid choice")