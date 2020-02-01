ll=int(input("Enter the lower limit:"))
ul=int(input("Enter the upper limit:"))
s=0

for no in range(ll,ul+1):
   if(no>1):
       for i in range(2,no):
           if(no%i==0):
               break
           else:
               print(no)
               s=s+no
print("sum of prime no:=",s)