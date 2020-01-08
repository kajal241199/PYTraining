try:
    #task 1
    bill = int(raw_input("enter bill amount : "))
    quantity = int(raw_input("enter quantity : "))
    rate = bill/quantity
    print("rate per kg : %0.2f")
except Exception as ex1:
    print(type(ex1)," : ", ex1 )

try:
    #task 2
    marks = [12, 23, 45, 56, 67, 66]
    rollno = int(input("enter roll no : "))
    print("marks of roll no %d is : %0.2f"%(rollno, marks[rollno-1]))
except Exception as ex2:
    print(type(ex2)," : ", ex2 )

try:
    #task 3
    file_name = raw_input("enter file name : ")
    fr = open(file_name)
    print(fr.read())
    fr.close()
except Exception as ex3:
    print(type(ex3)," : ", ex3 )

#end
print( "All is well" )