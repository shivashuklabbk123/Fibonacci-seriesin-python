n = int(input("Howmany term that you needed::"))
a=0
b=1
c=0
count = 1
print("The fibonacci series is :->")
while(count<=n):
    a=b
    b=c
    c = a+b
    count = count+1
    print( c , end = ",")
