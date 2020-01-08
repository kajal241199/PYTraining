books = []
for i in range(9):
    b_name = raw_input("enter the name of %d books: " %i)
    books.append(b_name)
sb = raw_input("enter a book to search: ")
for item in books:
    if item == sb:
       f = 1
if f == 1:
    print("book found")
else:
    print("not found")
