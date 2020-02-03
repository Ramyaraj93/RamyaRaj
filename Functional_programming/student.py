class student:
    def __init__(self,id,name,tot_marks):
        self.id=id
        self.name=name
        self.tot_marks=tot_marks
    def __str__(self):
        return self.name
lst=[]
try:
    f=open("/home/user/RamyaRaj/Functional_programming/student_data")
    for data in f:
        #data=f.rstrip("\n")
        #value=data.split(",")
        values=data.rstrip("\n").split(",")
        id=values[0]
        name=values[1]
        tot_marks=values[2]

        ob=student(id,name,tot_marks)
        lst.append(ob)

except Exception as e:
    print(e.args)

data=list(map(lambda ob:ob.name.upper(),lst))
for temp in data:
    print(temp)

data=list(filter(lambda ob:ob.str(tot_marks)>160,lst))
for t in data:
    print(str(t))








