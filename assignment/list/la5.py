numbers = [1, 2, 3, 4, 5, 6]
print( numbers )
s = min(numbers) 
numbers.remove(s)
k = min(numbers)
numbers.append(s)
print("second smallest no in list is %d: " %k) 
