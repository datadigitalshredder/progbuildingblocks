print('weekfourcheckpoint')

fahrenheit_value = float(input('What is the temperature in degrees fahrenheit?'))
celcius_value = (fahrenheit_value - 32) * 5 / 9
output = f'The temperature in degrees celcius is: {celcius_value:.1f}'

print(output)