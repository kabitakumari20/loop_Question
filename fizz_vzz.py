i=1
while i<=50:
    if i%3==0 and i%5==0:
        print(i,"fizzbuzz")
    elif i%3==0:
        print(i,"fizz")
    elif i%5==0:
        print(i,"buzz")
    else:
        print("nothing")
    i=i+1    
        
        