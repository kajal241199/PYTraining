score = [36, 45, 36, 78, 90]
duplicate = []
for item in score:
    if score.count(item)>1:
        duplicate.append(item)
else:
    print( duplicate )
    