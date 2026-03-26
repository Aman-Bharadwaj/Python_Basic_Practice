# Finding smallest number in a list
numbers = []

for i in range(10):
    numbers.append(int(input("Enter a number: ")))
    
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
        
print("Smallest", smallest)