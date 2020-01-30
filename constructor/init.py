
##############constructor(__init__)
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalues(self):
        print("name=",self.name)
        print("age=",self.age)
p=student("Ramya",25)
p.printvalues()