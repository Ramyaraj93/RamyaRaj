#class parent:
#    def phone(self):
#        print("I have nokia phone")
#class child(parent):
#    def phone(self):
#        print("iphone")

#c=child()
#c.phone()

########## method over riding
class person:
    def setperson(self,age,name):
        self.age=age
        self.name=name

    def printperson(self):
        print("name=",self.name)
        print("age=",self.age)

    def __str__(self):
        return self.name+str(self.age)

ob=person()
ob.setperson(25,"abhi")

print(ob)