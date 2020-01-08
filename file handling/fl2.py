#file operations
file_name = "actinfo.txt"

def add_act_info():
    'to add new account info'
    #creating/pening file in append mode
    w = open(file_name, "a")
    w.write(raw_input("enter account no: ")+"\t")
    w.write(raw_input("enter account name: ")+"\t")
    w.write(raw_input("enter account balance: ")+"\t")
    w.write(raw_input("enter account pin: ")+"\n")
    w.close()
    print("account info is added")

def read_act_info():
    'to read all accunt info'
    #opening fiile in reading mode
    r = open(file_name)
    #returns list of files from file
    lines = r.readlines()
    for line in lines:
        print(line)
    else:
        r.close()
#calling function
read_act_info()


