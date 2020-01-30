

class person:
    def setperson(self,age,name):
        self.age=age
        self.name=name

    def printperson(self):
        print("name=",self.name)
        print("age=",self.age)

class student(person):     #is_a relationship(student is a person)
    def setstudent(self,rol,course):
        self.rol=rol
        self.course=course