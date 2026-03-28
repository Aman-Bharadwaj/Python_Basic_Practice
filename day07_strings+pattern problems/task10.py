# Word count
s = input("Enter sentence: ")

count = 0
in_word = False

for ch in s:
    if ch != " ":
        if not in_word:
            count += 1
            in_word = True
    else:
        in_word = False
        
print("Words:", count)