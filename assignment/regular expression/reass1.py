import re
count = 0
s = raw_input("enter an input string : ")
print(s)
numbers = re.findall('[0-9]', s)
if numbers:
    print(numbers)
for i in s:
    if i.isdigit():
        count+=1
else:
    print(count)
