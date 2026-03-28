# Anagram check
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not Anagram")
else:
    is_anagram = True
    
    for ch in s1:
        count1 = 0
        count2 = 0
        
        for c in s1:
            if c == ch:
                count1 += 1
                
        for c in s2:
            if c == ch:
                count2 += 1
                
        if count1 != count2:
            is_anagram = False
            break
        
    if is_anagram:
        print("Anagram")
    else:
        print("Not Anagram")