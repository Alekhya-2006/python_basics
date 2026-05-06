# Match case - alternate for if-elif-else

color = input("enter color: ")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look and go slow") 
    case "Red":
        print("Stop")
    case _:
        print("Wrong color")           