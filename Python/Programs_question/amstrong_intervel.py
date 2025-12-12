num = int(input("Enter a num: "))

for x in range(1,num+1):
    result = 0
    temp = x
    while temp!=0:
        remainder = temp%10
        result = result + (remainder*remainder*remainder)
        temp=temp//10
    if(result==x):
        print(x)
