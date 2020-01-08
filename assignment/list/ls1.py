list = []
for i in range(9):
    marks = int(raw_input("enter the marrks of student %d: " %i))
    list.append(marks)
print( list )
print( max(list) )
print( min(list) )