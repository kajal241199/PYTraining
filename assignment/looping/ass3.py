# prg t0 print fibonacci series
sum = 0
n = int(raw_input("enter the no of elemnts"))
for i in range(n):
    print( i )
    sum += i
    print( sum )
else:
    print( "sum : %d  " %sum )