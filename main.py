from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from distance import meters_to_feet, feet_to_meters

celsius_temperature = 20
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature}°C is equal to {fahrenheit_temperature}°F")

fahrenheit_temperature = 68
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature}°F is equal to {celsius_temperature}°C")


meters_distance = 100
feet_distance = meters_to_feet(meters_distance)
print(f"{meters_distance} meters is equal to {feet_distance} feet")

feet_distance = 328.084
meters_distance = feet_to_meters(feet_distance)
print(f"{feet_distance} feet is equal to {meters_distance} meters")