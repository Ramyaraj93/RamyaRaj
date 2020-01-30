class person:
    def setvalues(self,age,name):
        self.age=age
        self.name=name
    def printvalues(self):
        print(self.age)
        print(self.name)
obj=person()
obj.setvalues(18,"ajay")
obj.printvalues()

obj1=person()
obj.setvalues(18,"vijay")
obj.printvalues()
