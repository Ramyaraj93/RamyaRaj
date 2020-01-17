num=int(input("Enter the no:"))

sum = 0
while (num != 0):
    digit = num % 10
    sum+=digit**3
    num = num // 10
print(sum)




