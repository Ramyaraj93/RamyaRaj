
############ prgm to find the sum of cubes of each digit of a no (12 = 1cube+2cube=1+8=9)

num=int(input("Enter the no:"))

sum = 0
while (num != 0):
    digit = num % 10
    sum+=digit**3
    num = num // 10
print(sum)




