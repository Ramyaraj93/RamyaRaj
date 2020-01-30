class student:
    def setvalues(self,name,roll_no,mark):
        self.name=name
        self.roll_no=roll_no
        self.mark=mark
    def printvalues(self):
        print(self.name)
        print(self.roll_no)
        print(self.mark)

obj=student()
obj.setvalues("Ramya",1,50)
obj.printvalues()

obj1=student()
obj1.setvalues("Soumya",1,55)
obj1.printvalues()
