
#line="KL32AB9076"
item=(input("Enter the vehregno")
rule="KL[0-9]{2}[A-Z]{2}[0-9]{4}"
import re

match=re.fullmatch("rule",item)

if (match!=None):
    print("Valid")
else:
    print("Invalid")