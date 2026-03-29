text = "programming"

vowels = "aeiou"
count = {}

for char in text:
    if char in vowels:
        count[char] = count.get(char, 0) + 1
        
print(count)