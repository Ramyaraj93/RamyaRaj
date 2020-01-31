ff=open("movies.txt","w")
fp=open("students_pass.txt","r")
ff=open("students_fail.txt","w")


set1=set()
set2=set()
set3=set()
for stud in fs:
    m=set(stud.split(","))
    print(m)


for stud_pass in fp:
    n=set(stud_pass.split(","))
    print(n)



set3=m.difference(n)
print(set3)












