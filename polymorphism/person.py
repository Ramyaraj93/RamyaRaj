f=open("/home/user/RamyaRaj/polymorphism/persn","r")
class staff:
    #def setvalues(self, age, name, sal):
    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.sal=sal

    def printstaff(self):
        print("name=",self.name)
        print("age=",self.age)

    def __str__(self):
        return self.name

lst=[]
for data in f:
    person=data.rstrip("\n").split(",")
    age=person[0]
    name=person[1]
    sal=person[2]
    #ob=staff()
    ob=staff(age,name,sal)  ##############
    #ob.setstaff(age,name,sal)
    lst.append(ob)

for data in lst:
    if(int(data.sal)>20000):
        print("Salary abv 20000 is",data.name)

max_count=0
min_count=0

for data in lst:
    if(int(data.sal)>20000):
        print("sal abv 20000=",data.name)
        max_count+=1
    else:
        min_count+=1
print("count whose salary>20000",max_count)
print("count whose salary<20000",min_count)



