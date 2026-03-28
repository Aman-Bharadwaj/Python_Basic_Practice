s = input("Enter string: ")

max_char = ""
max_count = 0

visited = ""

for ch in s:
    if ch not in visited:
        count = 0
        
        for c in s:
            if c == ch:
                count += 1
                
        if count > max_count:
            max_count = count
            max_char = ch
            
        visited += ch
        
print("Most frequent:", max_char)