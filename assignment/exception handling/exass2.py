try:
    name = raw_input("enter the name : ")
    age = int(raw_input("enter the age : "))
    for i in range(2):
        marks = [12, 23, 45, 56, 67, 66]
        rollno = int(input("enter roll no : "))
        print("marks of roll no %d is : %0.2f"%(rollno, marks[rollno-1]))
except ValueError as ve:
    print(type(ve)," : ", ve )
except Exception as ex:
    print(type(ex)," : ", ex)
    
        