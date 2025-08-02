FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32

def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def main():
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

if __name__ == "__main__":
    main()
