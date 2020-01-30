fs=open("students.txt","r")
fp=open("students_pass.txt","r")
ff=open("students_fail.txt","w")


set1=set()
set2=set()
set3=set()
for stud in fs:
    stud.split(",")
    set1.add(stud)
    print(set1)
for stud_pass in fp:
    stud_pass.split(",")
    set2.add(stud_pass)
    print(set2)

set3=set1.difference(set2)
print(set3)












