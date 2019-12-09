import random
for i in range(20):
    ch = ("G")
    no = random.randint(65,90)
    gen_ch = chr(no)
    if ch == gen_ch:
        print("yeah")
else:
        print("not lucky")
