text = input("Enter a string: ")

for i in range(len(text)):
    ascii_value = ord(text[i])

    if i % 2 == 0:
        ascii_value = ascii_value + 2
    else:
        ascii_value = ascii_value - 2

    new_character = chr(ascii_value)

    print(new_character, "ASCII value:", ascii_value)