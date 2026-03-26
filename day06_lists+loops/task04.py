# Removing Duplicates from list
numbers = [1, 2, 3 ,2, 3, 4]

new = []

for num in numbers:
    if num not in new:
        new.append(num)
        
print(new)