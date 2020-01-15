clothtype=int(input("Select cloth type:press 1 for cotton,2 for silk,3 for linen:"))
p_amt=int(input("Enter purchase amt:"))
if((clothtype==1)&(p_amt>20000)):
    print("10% discount")
elif((clothtype==1)&((p_amt>15000)&(p_amt<20000))):
    print("9% discount")
elif((clothtype==1)&((p_amt>14000)&(p_amt<15000))):
    print("7% discount")
elif((clothtype==1)&(p_amt<14000)):
    print("2% discount")

elif((clothtype==2)&(p_amt>20000)):
    print("15% discount")
elif((clothtype==2)&((p_amt>15000)&(p_amt<20000))):
    print("10% discount")
elif((clothtype==2)&((p_amt>14000)&(p_amt<15000))):
    print("9% discount")
elif((clothtype==2)&(p_amt<14000)):
    print("5% discount")

elif((clothtype==3)&(p_amt>20000)):
    print("15% discount")
elif((clothtype==3)&((p_amt>15000)&(p_amt<20000))):
    print("10% discount")
elif((clothtype==3)&((p_amt>14000)&(p_amt<15000))):
    print("9% discount")
elif((clothtype==3)&(p_amt<14000)):
    print("5% discount")

