act_username = "sholey"
act_password = 1998

username = input("Username: ")
password = int(input("Password: "))

if username == act_username and password == act_password:
    print("Login successful") 

elif password != act_password:
    print("wrong Password")

else:  
    print("Wrong Username")
    print("Enter a valid username")     