# Looping through string
s = "abc"

for ch in s:
    print(ch)
    
# Strings are immutable
s = "hello"
s = "H" + s[1:]
print(s) #Hello