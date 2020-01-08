names = ["kajal", "ishi", "deepak", "dimple", "ketan", "garvita", "zeel", "rekha", "raj", "alpha"]
vowels = 0
for item in names:
    for ch in item:
        if ch in "AEIOUaeiou":
            vowels += 1
    else:
        print("no of vowels in %s is %d " %(item, vowels))
    vowels = 0
