# num=int(input("enter the num="))
# i=1
# while i<=num:
#     num1=int(input("enter the num="))
#     j=1
#     sum=0
#     while j<num1:
#         if num1%j==0:
#             sum=sum+j
#         j=j+1
#     i=i+1
#     print(sum)
#     if sum==num1:
#         print(sum,"it is perfect")
#     else:
#         print(sum,"it is not perfect")

# num=int(input("enter the num="))
# i=1
# while i<=num:



# a=int(input("enter the a="))
# b=int(input("enter the b="))
# i=1
# gcd=0
# while i<a:
#     if a%i==0 and b%i==0:
#         gcd=i
#     i=i+1
# print(gcd)


# x=int(input("enter the num="))
# y=int(input("enter no--"))
# i=0
# lcm=x*y
# while x!=y:
#     if x>y:
#         x-=y
#     else:
#         y-=x
# lcm=lcm//y
# print(lcm)

# a,b,c=input().split()
# x=int(a)
# y=int(b)
# z=int(c)
# if x>y and x>z:
#     print(x,"iss max")
# elif y>x and y>z:
#     print(y,"is max")
# else:
#     print(z,"is max")


num=int(input("enter the num="))
if num%3!=0:
    print("-1")
elif num%2==0 and num%3==0:
    print("0")
elif num%3==0:
    print("1")
else:
    print("nothing")
