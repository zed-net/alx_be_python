# weather_advice.py

# Prompt the user for weather input using the specified string.
# The input() function reads a line from input, converts it to a string, and returns that.
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Convert the input to lowercase to make the comparison case-insensitive.
# This ensures that "Sunny", "SUNNY", or "sunny" are all treated the same.
weather_lower = weather.lower()

# Use conditional statements (if, elif, else) to provide clothing recommendations.

# If the weather is "sunny"
if weather_lower == "sunny":
    print("Wear a t-shirt and sunglasses.")
# Else if the weather is "rainy"
elif weather_lower == "rainy":
    print("Don't forget your umbrella and a raincoat.")
# Else if the weather is "cold"
elif weather_lower == "cold":
    print("Make sure to wear a warm coat and a scarf.")
# Else (if none of the above conditions are met, meaning unexpected input)
else:
    print("Sorry, I don't have recommendations for this weather.")


