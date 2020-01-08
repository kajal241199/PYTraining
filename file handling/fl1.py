#creating new file and store some details
#creating/opening file to write info
fw = open("empinfo.txt", "w")
print( type(fw) )
#writing data into file
fw.write("120001\n")
fw.write("kajal singhvi\n")
fw.write(raw_input("enter salary: "))
fw.write("\n")
fw.write(raw_input("enter address: "))
fw.close()
print("data written into file")
#opening file into reading mode 
fr = open("empinfo.txt")
#reading all file data
data = fr.read()
fr.close()
print("file data: ")
print( data )

