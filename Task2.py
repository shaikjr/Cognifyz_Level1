#Task2: Temperature Conversion

#Create a Python program that converts
#temperatures between Celsius and
#Fahrenheit. Prompt the user to enter a
#temperature value and the unit of
#measurement, and then display the
#converted temperature.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

