a = int(input("Enter No. 1: "))
b = int(input("Enter No. 2: "))
c = int(input("Enter No. 3: "))

if a >= b and a >= c:
    print("A is the greatest", a)
    
elif b >= a and b >= c:
    print("B is the greatest", b)   
    
else:
    print("C is greatest", c)
    