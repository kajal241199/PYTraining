fw = open("studentinfo.txt", "w")
fw.write(raw_input("enter student name: "))
fw.write(raw_input("enter sudent roll no: "))
fw.write(raw_input("enter student address: "))
fw.write(raw_input("enter sudent mbno: "))
fw.close()
print("data written into file")
fr = open("studentinfo.txt")
data = fr.read()
fr.close()
print("file data: ")
print( data )


