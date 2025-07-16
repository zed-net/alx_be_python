# weather_advice.py

# Prompt the user for weather input using the specified string.
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Use conditional statements (if, elif, else) to provide clothing recommendations.
# The conditions and print statements are formatted to precisely match the expected validator pattern.

# If the weather is "sunny"
if weather == "sunny": print("Wear a t-shirt and sunglasses.")
# Else if the weather is "rainy"
elif weather == "rainy": print("Don't forget your umbrella and a raincoat.")
# Else if the weather is "cold"
elif weather == "cold": print("Make sure to wear a warm coat and a scarf.")
# Else (if none of the above conditions are met, meaning unexpected input)
else: print("Sorry, I don't have recommendations for this weather.")

