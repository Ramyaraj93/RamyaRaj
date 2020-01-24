lst=[1,5,8,4]
lst=sorted(lst)
print(lst)
len=len(lst)
lower=0
upper=len-1
num=int(input("Enter the no"))
while(lower<upper):
    if(lst[lower]+lst[upper]==num):
        print(lst[lower],lst[upper])
        break
    elif(lst[lower]+lst[upper]<num):
        lower+=1
    elif(lst[lower]+lst[upper]>num):
        upper-=1
else:
    print("No pair")

##############
lst=[1,2,3,4,5,6]

low=0
upp=len(lst)-1
num=int(input("Enter the no"))
while(lower<upper):
    sum=lst[low]+[upp]
    if(sum<num):
       low+=1
    elif(lst[lower]+lst[upper]<num):
        lower+=1
    elif(lst[lower]+lst[upper]>num):
        upper-=1
else:
    print("No pair")
