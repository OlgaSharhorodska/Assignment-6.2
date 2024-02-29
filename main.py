from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

celsius_temperature = 20
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature}°C is equal to {fahrenheit_temperature}°F")

fahrenheit_temperature = 68
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature}°F is equal to {celsius_temperature}°C")