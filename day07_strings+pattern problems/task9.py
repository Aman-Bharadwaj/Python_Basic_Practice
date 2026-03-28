# Replace vowels with *
x = input("Enter string: ")

vowels = "aeiouAEIOU"
result = ""

for ch in x:
    if ch in vowels:
        result += "*"
    else:
        result += ch
        
print(result)