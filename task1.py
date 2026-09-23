text = input("Enter a string: ")

for i in range(len(text)):
    if text.count(text[i]) == 1:
        print("First non-repeated character:", text[i])
        print("Position:", i)
        break
else:
    print("Every character is repeated.")