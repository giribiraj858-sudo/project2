celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", round(fahrenheit, 2))

if celsius < 15:
    print("Temperature Level: Cold")
elif celsius <= 30:
    print("Temperature Level: Normal")
else:
    print("Temperature Level: Hot")