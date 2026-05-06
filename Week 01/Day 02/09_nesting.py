act_username = "sholey"
act_password = 1998

username = input("Username: ")
password = int(input("Password: "))

if username == act_username and password == act_password:
    print("Login successful") 
    
else:  
    # nesting
    if username != act_username:
        print("Wrong Username")
        print("Enter a valid username")
    else:
        print("Wrong Password")
        print("Please enter correct password")    