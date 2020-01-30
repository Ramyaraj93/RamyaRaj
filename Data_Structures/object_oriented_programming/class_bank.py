import datetime
class bank:
    bname="sbi"
    def create_Account(self,b_name,ac_no):
        self.min_bal=3000
        self.b_name=b_name
        self.ac_no=ac_no
        self.bal=self.min_bal


    def deposit(self):
        amt=int(input("Enter the amt you want to deposit"))
        self.bal+=amt
        print("your",bank.bname,"has been deposited with amt=",amt,"on",datetime)

        print("your avail bal=",self.bal)
    def withdraw(self):
        amt1=int(input("Enter amount to be withdrawn"))
        if self.min_bal>=amt1:
            self.bal-=amt1
            print("Withdraw",amt1)
        else:
            print("Insufficient balance")
    def bal_enq(self):
        print("balance amt",self.bal)


ob = bank()

ob.create_Account("sbi",1001)
ob.deposit()




ob1=bank()
ob1.create_Account("sbi",1002)



