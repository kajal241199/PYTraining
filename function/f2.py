# defining function
def loan_el_amt(salary, bonus , fd=10000):
    'to calc loan eligibility amount'
    if salary >= 20000:
        loan = salary*6
    else:
        loan = salary*4
    if bonus >= 10000:
        loan += bonus*3
    else:
        loan += bonus*2
    loan += fd*.5
    return loan

def sum_dig_str(str):
    'to find the sum of digir=t in a string'
    digit = 0
    for ch in str:
        if ch in "0123456789":
            ch = int(ch)
            digit += ch
        
    print( digit )

# required arguments (positional order)
amt = loan_el_amt(25000, 12000, 60000)
print("enjoy,loan upto : %0.2f rs " %amt)
#keyword arguments ( names of parameters)
amt = loan_el_amt(bonus=9000, fd=100000, salary=16000)
print("enjoy, loan upto: %0.2f rs" %amt)
#default argument
amt = loan_el_amt(bonus=5000, salary=15000)
print("enjoy, loan upto : %0.2f rs" %amt)

sum_dig_str("kajal123")

