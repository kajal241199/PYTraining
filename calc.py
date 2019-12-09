# calculating call cost
import math
duration = 130
rate = 1.5
mins = math.ceil(duration/60)
cost = mins*rate*1.1
print("call cost is:",cost)
# print