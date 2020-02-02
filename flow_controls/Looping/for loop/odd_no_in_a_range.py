#### to find the odd no:s b/w a range

ll = int(input("Enter the start of range: "))
ul = int(input("Enter the end of range: "))

# iterating each number in list
for num in range(ll,ul+1):

    # checking condition
    if num % 2 != 0:
        print(num)   ###### o/p will be in diff lines
        #print(num, end=" ")  #### o/p will be in single line seperated by space