try:
    mb = int(raw_input("enter the mobile no:"))
    print( mb )
except ValueError as ve:
    print(type(ve)," : ", ve )