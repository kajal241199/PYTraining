info = input("enter text: ")
digit, alpha, spaces, symbols = 0, 0, 0, 0
for ch in info:
    if ch.isalpha():
        alpha+=1
    elif ch.isdigit():
        digit+=1
    elif ch.isspace():
        spaces+=1
    else:
        symbols+=1
else:
    print(alpha,digit,spaces,symbols)
    size = len(info)
    if symbols <= size*0.2:
        print("means")
    else:
        print("nomeans")