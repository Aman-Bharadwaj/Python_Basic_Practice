numbers = [10, 50, 32, 87, 20]

max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
        
print("Max", max_num)