class budget:
    def __init__(self,date,expenditure,amt):  ####### constructor
        self.date=date
        self.expenditure=expenditure
        self.amt=amt
#    def __str__(self):
#        return self.name
lst=[]
try:
    f=open("/home/user/RamyaRaj/list_comprehension/Budget_details")
    for data in f:
        #data=f.rstrip("\n")
        #value=data.split(",")
        values=data.rstrip("\n").split(",")
        print(values)
        date=values[0]
        expenditure=values[1]
        amt=values[2]

        ob=budget(date,expenditure,amt)
        lst.append(ob)

except Exception as e:
    print(e.args)

date=list(map(lambda ob:ob.date[0]=='02/02/2020',lst))
for t in date:
    print(t)

