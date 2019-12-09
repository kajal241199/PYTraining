fruits = [2.5, 5, 5.6, 7, 5.9, 1]
print(fruits)
sum = 0
for item in fruits:
    sum += item
else:
        bill = sum*60
        print("pay bill is %0.2f rs for %0.2f kg fruits"% (bill,sum))
        #indexing/slicing/ranging
        print(fruits[3])
        print(fruits[-2])
        print(fruits[1:4])
        print(fruits[2: ])
        #adding new items
        fruits.append(1.5)
        print(fruits)
        #deleting an item
        del fruits[3]
        print(fruits)
        #update an item
        fruits[2] = 2.25
        print(fruits)    
        #functions
        #return size of givenn list
        print(len(fruits))
        #returns larget vavlue in list
        print(max(fruits))
        #smallest in list
        print( min(fruits))
        #print as a list of given string
        ls = list("INDIA")
        print(ls)
