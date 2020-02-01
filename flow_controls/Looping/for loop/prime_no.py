#
# no=int(input("Enter the no:"))
# flg=0
# for i in range(2,no):
#     if(no%i==0):
#         flg=flg+1
#         break
#     else:
#         flg=0
# if(flg==0):
#     print("Its a prime")
# else:
#     print("Not a prime")



##### prgm to check wheather a no is prime or not

# no=int(input("Enter the no:"))
# flg=0
# for i in range(2,no):
#     if(no%i==0):
#         flg=flg+1
#         break
#     else:
#         flg=0
# if(flg==0):
#     print("Its a prime")
# else:
#     print("Not a prime")


number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")

