num=int(input())
i=0
while i<num:
    num1=int(input())
    j=0
    l=len(str(num1))
    sum=0
    while j<l:
        r=num1%10
        sum=sum+r
        num1//=10
        j=j+1
    print(sum)
    i=i+1