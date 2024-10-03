def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_converter():
    temp = float(input("Enter the temperature value: "))
    original_scale = input("Enter the original scale (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    if original_scale == 'C':
        fahrenheit = celsius_to_fahrenheit(temp)
        kelvin = celsius_to_kelvin(temp)
        print(f"{temp}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f}K.")
    
    elif original_scale == 'F':
        celsius = fahrenheit_to_celsius(temp)
        kelvin = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F is equal to {celsius:.2f}°C and {kelvin:.2f}K.")
    
    elif original_scale == 'K':
        celsius = kelvin_to_celsius(temp)
        fahrenheit = kelvin_to_fahrenheit(temp)
        print(f"{temp}K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F.")
    
    else:
        print("Invalid input! Please enter a valid scale (C, F, or K).")

# Run the converter
temperature_converter()
