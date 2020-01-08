class point:
    'to describe/represent co-ordinate point by x, y, z'

    def __init__(self, x, y, z):
        'to initialise a point'
        self.X = float(raw_input("enter X : "))
        self.Y = float(raw_input("enter Y : "))
        self.Z = float(raw_input("enter Z : "))

    def  __str__(self):
        'to display an object'
        str="X : %0.2f\tY : %0.2f\tZ : %0.2f" %(self.X,self.Y,self.Z)
        return str

    def __add__(self, other):
        'to add 2 instances of point'
        if type[other]


#creating list to store point's instances
pts = []
for i in range (3):
    #creating an instance and append nto list
    pts.append( point() )
for item in pts:
    print( item )
