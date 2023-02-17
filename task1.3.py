word = input("Enter the word: ")
n = len(word)
res = list(word)
for i in range (n-1, -1, -1):
    print(res[i],end ="")
