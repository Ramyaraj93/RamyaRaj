class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):    #used to over_ride '+' operator
        #return(self.pages+other.pages)
        return Book(self.pages + other.pages)

    def __sub__(self, other):
        return Book(self.pages - other.pages)

    def __mul__(self, other):
        return Book(self.pages * other.pages)

    def __truediv__(self, other):
        return Book(self.pages / other.pages)

    def __str__(self):
        return str(self.pages)

b=Book(100)
b1=Book(200)
b2=Book(300)
#print(b+b1)    ###b and b1 are book objects
print(b+b1+b2)
print(b-b1-b2)
print(b*b1*b2)
print(b/b1/b2)