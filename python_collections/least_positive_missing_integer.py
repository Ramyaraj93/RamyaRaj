st={-1,-2,0,2,1,3,4,-3}
lst=list(st)
lst.sort()
print(lst)
no=1
lst1=list()
for i in lst:
    if(i>0):
        lst1.append(i)
print(lst1)
low=0
flg=0
upper=(len(lst1)-1)
while(low<=upper):
    if(no==lst1[low]):
        low=low+1
        no+=1
    elif(no!=lst[low]):
        flg=flg+1
        break
print("least positive missing no=",no)