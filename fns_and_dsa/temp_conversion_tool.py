FAHRENHEIT_TO_CELSIUS_FACTOR = float((5/9))
CELSIUS_TO_FAHRENHEIT_FACTOR = float((9/5))

def convert_to_celsius(fahrenheit):
    temp = ((fahrenheit- 32) * FAHRENHEIT_TO_CELSIUS_FACTOR )
    print(f"{fahrenheit}°F is {temp} °C")

def convert_to_fahrenheit(celsius):
    temp = ((celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32)
    print(f"{celsius}°C is {temp} °F")

user_temp = float(input("Enter the temperature to convert:"))
degree = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
if degree == "C":
    convert_to_fahrenheit(user_temp)
elif degree == "F":
    convert_to_celsius(user_temp)
else:
    print("Invalid operation")
