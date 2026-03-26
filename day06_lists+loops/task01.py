# Sum of all numbers in a list
numbers = []

for i in range(10):
    numbers.append(int(input("Enter a number: ")))     
    
print("Sum", sum(numbers))