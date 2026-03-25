numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    
    if num % 2 == 0 and num > 10:
        numbers.append(num)
    
print(numbers)