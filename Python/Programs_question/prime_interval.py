interval = int(input("Enter a num: "))
for x in range(2,interval+1):
    i=2
    while i<x:
        if x%i==0:
            break
        i += 1
    else:
        print(x)
    

  