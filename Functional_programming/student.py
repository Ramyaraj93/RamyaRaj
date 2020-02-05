class student:
    def __init__(self,id,name,tot_marks):  ####### constructor
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

anames=list(filter(lambda ob:ob.name[0]=='A',lst))
for names in anames:
    print("anames",names)


passed=list(filter(lambda ob:int(ob.tot_marks)>160,lst))
for stud in passed:
    print("Students who passed:",stud)


high_mark=max((ob.tot_marks,ob.name,ob.id) for ob in lst)
print(high_mark)
#print(type(high_mark))  ######### based on first argument(tot_marks) it works

###### if more than 1 student has highest mark,to print the details of both students
high_mark=max(ob.tot_marks for ob in lst)
lst3=[(ob.name,ob.tot_marks,ob.id) for ob in lst if ob.tot_marks==high_mark]
print(lst3)










