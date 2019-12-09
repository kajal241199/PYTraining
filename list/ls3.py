#creating list to store marks
marks = [95, 82.5, 75, 86, 64, 95]
#adding new item
marks.append(72)
print( marks )
# returns no of occurences into list
print( marks.count(95))
batch = [82, 66]
#extending list by given list
marks.extend( batch)
print( marks )
#returns an index of given item
print( marks.index(75) )
# inserting an item at speified index
marks.insert(2, 65)
print( marks )
# remove last item if index is not there
marks.pop(3)
print( marks )
#remove given item from list
marks.remove(64)
print( marks )
# reversing list
marks.reverse()
print( marks )
# sorting list in descending order
marks.sort(reverse=True)
print( marks)