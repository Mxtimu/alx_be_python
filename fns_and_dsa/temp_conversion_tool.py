FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def main():
    temperature_input = input("Enter the temperature to convert: ")
    try:
        temperature = float(temperature_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if unit.upper() == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    elif unit.upper() == 'C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:
        print("Invalid unit. Please enter C or F.")


if __name__ == "__main__":
    main()