ori_num = int(input("Enter a num: "))
result=0
num = ori_num
while num!=0:
    remainder = num%10
    result = result + (remainder*remainder*remainder)
    num=num//10
print(result)
if result==ori_num:
    print("Armstrong Number")
else:
    print("Not an amstrong number")