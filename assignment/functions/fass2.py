#fun to count no of upper and lower case alphabets in a string
def calc_ul(str):
    l = 0
    u = 0
    for ch in str:
       if ch == ch.lower:
           l += 1
       else:
           u += 1
    print("no of lower cases : %d and upper cases is: %d" %(l,u))

#fun call
calc_ul("KAJAL")