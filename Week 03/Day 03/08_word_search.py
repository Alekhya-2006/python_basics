with open("file.txt", "r") as f:

    found = False
    count = 0

    while True:
    
        data =  f.readline()

        if not data:
            break

        count += 1

        if "demo" in data:
            print("Found at line:", count)
            found = True
            break

    if not found:
        print("The word was not found")   