# # Reversing a string
# s = input("Enter string: ")

# rev = ""
# for ch in s:
#     rev = ch + rev
    
# print("Reversed", rev)

# # Counting vowels
# v = input("Enter string: ")

# count = 0
# vowels = "aeiouAEIOU"

# for ch in v:
#     if ch in vowels:
#         count += 1
    
# print("Vowels", count)

# # Removing spaces
# e = input("Enter string: ")

# result = ""
# for ch in e:
#     if ch != " ":
#         result += ch

# print(result)

# Uppercase without .upper()

u = input("Enter string: ")

result = ""

for ch in u:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch
        
print(result)