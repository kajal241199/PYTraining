books = [java, c, python, c++, java]
duplicate = []
for item in books:
    if books.count(item)>1:
        duplicate.append(item)
else:
    print( duplicate )
    