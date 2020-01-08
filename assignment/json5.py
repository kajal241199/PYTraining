import json
file_name = "emp.json"

def read_info():
    'to read emp detail'
    fr = open(file_name) 
    # reading all data of json file
    data = json.load(fr)
    for item in data:
        print("%d\t%s\t%0.2f" %(item["EC"], item["EC"], item["ES"]))
    fr.close()

def add_info():
    'to add new emp detail'
    fr = open(file_name)
    data= json.load(fr)
    fr.close()
    ec = int(input("enter ecode: "))
    en = input("enter name: ")
    es = float(raw_input("enter esalary: ")
    # creating dict to parse  into json object
    info = {"EC":ec, "EN":en, "ES":es}
    #appending/adding into list
    data.append(info)
    #opening file in write mode
    fw = open("file-name", "w")
    #dumping list(data) into json file
    json.dump(data, fw)
    fw.close()
    #calling function
    add_info()
    read_info()