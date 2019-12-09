# string task
info = " Kajal@24"
digits,alpha,spaces,symbols = 0, 0, 0, 0
for ch in info:
    if ch.isalpha():
        alpha+=1
    elif ch.isspace():
        spaces+=1
    elif ch.isdigit():
        digits+=1
    else:
        symbols+=1
else:
    print("alpha : %d\ndigits : %d\nspaces : %d\n  symbols : %d" %(alpha ,digits, spaces, symbols))
    # returns size
size = len(info)
print(size)
if  symbols >= size*0.2:
    print("string is not meaningful")
else:
    print("string is meaningful")