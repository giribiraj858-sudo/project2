number = int(input("Enter a positive integer with at least 3 digits: "))

if number <= 0:
    print("Please enter a positive number")
elif len(str(number)) < 3:
    print("Please enter a number with at least 3 digits.")
else:
    print("Decimal:", (number))
    print("Binary:", bin(number))
    print("Octal:", oct(number))
    print("Hexadecimal:", hex(number))
    print("Last digit:", number % 10)

    if number % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd") 