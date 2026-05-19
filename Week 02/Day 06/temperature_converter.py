# Temperature Converter using Static Method
# Concept:  @staticmethod

class Temperature:

    @staticmethod
    def convert_temperature(temp, degree):

        # Celsius to Fahrenheit
        if degree == "F":
            return ((9/5) * temp) + 32  
        
        # Fahrenheit to Celsius
        elif degree == "C":
            return (temp - 32) * (5/9)
        
        else:
            return "Invalid Option"

temp = int(input("Enter the Temperature: "))

print("\nConvert to Celsius (C)")
print("Convert to Fahrenheit (F)")

deg = input("Choose option (C/F): ").upper()

print("Converted Temperature =",
      Temperature.convert_temperature(temp, deg))