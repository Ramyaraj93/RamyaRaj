m1=int(input("Enter mark of subject1"))
m2=int(input("Enter mark of subject2"))
m3=int(input("Enter mark of subject3"))

m=m1+m2+m3

if(m>145):
    print("grade of student is A+")
elif((m>140)&(m<145)):
    print("grade of student is A")
elif((m>135)&(m<140)):
    print("grade of student is B+")
elif((m>130)&(m<135)):
    print("grade of student is B")
else:
    print("Fail")

