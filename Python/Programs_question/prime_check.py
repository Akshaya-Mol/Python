num = int(input("Enter Num : "))
if num==0 or num==1:
    print("Neither Prime nor Composite")
elif num == 2:
    print("Prime Number")
elif num%1==0 and num%num==0 and num%2!=0:
    print("Prime number")
else:
    print("Not a prime number")