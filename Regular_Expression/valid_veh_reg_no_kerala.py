import re
line="KL32AB9076"
#line=(input("Enter the var")
rule='KL[0-9]{2}[A-Z]{2}[0-9]{4}'

match=re.match(rule,line)

if (match!=None):
    print("Valid")
else:
    print("Invalid")