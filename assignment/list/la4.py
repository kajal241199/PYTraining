list = ["java", "c", "python","java","python"]
print( list )
duplicate = []
for item in list:
    if list.count(item) > 1:
        duplicate.append(item)
print( duplicate )