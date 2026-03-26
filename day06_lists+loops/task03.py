# Printing only odd numbers
odd_numbers = []

for i in range(10):
    odd_numbers.append(int(input("Enter a number: ")))
 
for num in odd_numbers:
    if num % 2 != 0:
        print(num)
    
