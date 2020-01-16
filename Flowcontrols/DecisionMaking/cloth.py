clothtype=int(input("Select cloth type:press 1 for cotton,2 for silk,3 for linen:"))
p_amt=int(input("Enter purchase amt:"))
if((clothtype==1)&(p_amt>20000)):
    p_amt = int(input("Enter purchase amt:"))
    print("10% discount")
    f_amt=p_amt-(p_amt*0.10)
    print("Amt to be paid by the customer",f_amt)
elif((clothtype==1)&((p_amt>15000)&(p_amt<20000))):
    p_amt = int(input("Enter purchase amt:"))
    print("9% discount")
    f_amt = p_amt - (p_amt * 0.09)
    print("Amt to be paid by the customer", f_amt)
elif((clothtype==1)&((p_amt>14000)&(p_amt<15000))):
    p_amt = int(input("Enter purchase amt:"))
    print("7% discount")
    f_amt = p_amt - (p_amt * 0.07)
    print("Amt to be paid by the customer", f_amt)
elif((clothtype==1)&(p_amt<14000)):
    p_amt = int(input("Enter purchase amt:"))
    print("2% discount")
    f_amt = p_amt - (p_amt * 0.02)
    print("Amt to be paid by the customer", f_amt)

elif((clothtype==2)&(p_amt>20000)):
    p_amt = int(input("Enter purchase amt:"))
    print("15% discount")
    f_amt = p_amt - (p_amt * 0.15)
    print("Amt to be paid by the customer", f_amt)
elif((clothtype==2)&((p_amt>15000)&(p_amt<20000))):
    p_amt = int(input("Enter purchase amt:"))
    print("10% discount")
    f_amt = p_amt - (p_amt * 0.10)
    print("Amt to be paid by the customer", f_amt)
elif((clothtype==2)&((p_amt>14000)&(p_amt<15000))):
    p_amt = int(input("Enter purchase amt:"))
    print("9% discount")
    f_amt = p_amt - (p_amt * 0.09)
    print("Amt to be paid by the customer", f_amt)
elif((clothtype==2)&(p_amt<14000)):
    p_amt = int(input("Enter purchase amt:"))
    print("5% discount")
    f_amt = p_amt - (p_amt * 0.05)
    print("Amt to be paid by the customer", f_amt)

elif((clothtype==3)&(p_amt>20000)):
    p_amt = int(input("Enter purchase amt:"))
    print("15% discount")
    f_amt = p_amt - (p_amt * 0.15)
    print("Amt to be paid by the customer", f_amt)
elif((clothtype==3)&((p_amt>15000)&(p_amt<20000))):
    p_amt = int(input("Enter purchase amt:"))
    print("10% discount")
    f_amt = p_amt - (p_amt * 0.10)
    print("Amt to be paid by the customer", f_amt)
elif((clothtype==3)&((p_amt>14000)&(p_amt<15000))):
    p_amt = int(input("Enter purchase amt:"))
    print("9% discount")
    f_amt = p_amt - (p_amt * 0.09)
    print("Amt to be paid by the customer", f_amt)
elif((clothtype==3)&(p_amt<14000)):
    p_amt = int(input("Enter purchase amt:"))
    print("5% discount")
    f_amt = p_amt - (p_amt * 0.05)
    print("Amt to be paid by the customer", f_amt)
else:
    print("Invalidno")
