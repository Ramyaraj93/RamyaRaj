
import re
count=0
#x='a+'################### contins count of a
#x='a*' ################ checks every location (both a location abd zero a location)
#x='a?'######### each positon -count of a including zero no: of a(individually count of a,not sequential count)
#x='a{2}'############ only two a's
#x='a{2,3}'####### min 2 max3
#x='^a'####### checks whether starting with a
x='a$'######### checks whether ending with a
matcher=re.finditer(x,'abaabaaabacaab')
for match in matcher:

    print("match available at",match.start())
    print("group=",match.group())
    count+=1
print("count=",count)
