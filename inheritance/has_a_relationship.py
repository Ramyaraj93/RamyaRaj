

class person:
    def setperson(self,age,name):
        self.age=age
        self.name=name

    def printperson(self):
        print("name=",self.name)
        print("age=",self.age)

class student(person):
    def setstudent(self,rol,course):
        self.rol=rol
        self.course=course
    def printDetails(self):
        print("rol=",self.rol)
        print("course=", self.course)


ob=student()
ob.setperson(25,"abhi")
ob.setstudent(1000,"mca")
ob.printperson()