employee=[[10,"ajay",15000],[11,"vijay",15000],[12,"saj",25000]]

for emp in employee:
    if(emp[2]>15000):
        print(emp[1])
    else:
        print("not found")
