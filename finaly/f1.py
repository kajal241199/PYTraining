fr = None
try:
    file_name = raw_input("enter filename : ")
    #opening file in read mode
    fr = open(file_name)
    lines = fr.readlines()
    balance = float(lines[2])
    no = int(raw_input("enter no of persons to divide : "))
    rs = balance/no
    print("rs per person is : %0.2f rs" %rs)
    print("task done")
except Exception as ex:
    #action code
    print(type(ex), " : ", ex)
finally:
    #code ot release resource
    if fr:
        fr.close()
        print("file closed")
print("all is well")
