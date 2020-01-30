class parent:
    def phonee(self):
        print("I have nokia 1100")

class child(parent):
    def phone(self):
        print("I have i phone")

c=child()

c.phone()
c.phonee()

p=parent()
p.phonee()


class person:
    def setperson(self,age,name):
        self.age=age
        self.name=name

    def printperson(self):
        print("name"=self.name)
        print("age" = self.age)

class student:
    def setstudent(self,rol,course):
        self.rol=rol
        self.course=course