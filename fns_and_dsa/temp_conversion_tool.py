# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_FREEZING_POINT = 32

def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    float: The temperature in Celsius.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_FREEZING_POINT
    return (fahrenheit - FAHRENHEIT_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Parameters:
    celsius (float): The temperature in Celsius.

    Returns:
    float: The temperature in Fahrenheit.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FAHRENHEIT_FREEZING_POINT
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_FREEZING_POINT

def main():
    try:
        temp = float(input("Enter the temperature: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp:.2f}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
