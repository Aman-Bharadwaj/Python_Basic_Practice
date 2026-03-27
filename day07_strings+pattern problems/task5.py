# Palindrome Checker
s = input("Enter string: ")

is_palindrome = True

for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        is_palindrome = False
        break
    
if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")
    
# Character Frequency

# c = input("Enter string: ")

# for ch in c:
#     if c.count(ch) > 0:
#         print(ch, ":", c.count(ch)) # Print duplicate
        
# Better one
c = input("Enter string: ")

visited = ""

for ch in c:
    if ch not in visited:
        count = 0
        for k in c:
            if k == ch:
                count += 1
        print(ch, ":", count)
        visited += ch
        
# Remove Duplicate Characters
s = input("Enter string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch
        
print(result)

# Word count
q = input("Enter string: ")

count = 0
in_word = False

for ch in q:
    if ch != " ":
        if not in_word:
            count += 1
            in_word = True
        else:
            in_word = False
            
print("Words:", count)