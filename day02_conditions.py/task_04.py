input = int(input("Enter a number: "))
if input % 3 == 0 and input % 5 == 0:
    print("Fizzbuzz")
elif input % 3 == 0:
    print("Fizz")
elif input % 5 == 0:
    print("Buzz") 
elif input % 7 == 0:
    print("Boom")
else:
    print(input)   
