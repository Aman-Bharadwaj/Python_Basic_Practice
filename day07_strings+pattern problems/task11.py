s = input("Enter sentence: ")

words = []
word = ""

for ch in s:
    if ch != " ":
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""

if word != "":
    words.append(word)
    
result = ""
for i in range(len(words)-1, -1, -1):
    result += words[i] + " "
    
print(result.strip())