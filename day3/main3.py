# main.py

import temp_utils

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Choose conversion (1 or 2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        f = temp_utils.celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is {f:.2f}°F")

    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        c = temp_utils.fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {c:.2f}°C")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
