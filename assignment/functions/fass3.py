# fun to print words in hypen separated sequence
def print_hsw(str): 
    str = [ n for n in str.split('-')]
    str.sort()
    print( '-'.join(str) )
   
#fun call
print_hsw("my-name-is-kajal")
