import math
import re
class basic:
    'to define basic operations'

    def areacylinder(self,radius,height)
    'to calc area of cylinder'
    area = math.pi*radius*height
    print("area of cylinder is : %0.2f cm" %area)


    def countsymbols(self, str)
    'to count special symbols'
    symbols = re.findall('[^a-z0-9]',str,re.I)
    print("siz : %0.2f cm" %area)

#inheriting base class
class advanced(basic):
    'to define new operatons'
 
    def getnumbers(Self):
        'to extract all numbers from str'
        str = input("enter string : ")
        numbers = re.findall('\d+[.]?\d*', str)
        print( numbers )

#creating an instance
ad1 = advance()
ad1.areacylinder(20, 40)
ad1.countsymbols("Gits@2020$4010 #12 ^ram&")
ad1.getnumbers()