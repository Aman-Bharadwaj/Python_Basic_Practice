text =  "Apple banana apple Mango banana Apple"

words = text.lower().split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1
     
print(count)