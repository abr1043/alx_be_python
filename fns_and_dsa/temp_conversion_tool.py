def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "C":
    converted = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted:.2f}°F")
elif unit == "F":
    converted = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is {converted:.2f}°C")
else:
    print("Invalid unit. Please enter C or F.")
