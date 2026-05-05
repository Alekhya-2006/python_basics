# program 07: Ask user for temperature in Celsius(String input)
# Convert to float, then calculate and print temperature in Fahrenheit

celsius_temp = input("Enter the temperatuere in Celsius: ")
celsius_temp = float(celsius_temp)

fahrenheit_temp = (celsius_temp * (9/5)) + 32
print("The temperature in Fahrenheit is ",fahrenheit_temp)