# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def temp_convert():
    temp = float(input("Enter the temperature to convert: "))
    temp_scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    
    if temp_scale == "F":
        result = convert_to_celsius(temp)
        print(f"{temp}°F is {result:.2f}°C")
    elif temp_scale == "C":
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result:.2f}°F")
    else:
        print("Invalid temperature. Please enter a numeric value.")

temp_convert()