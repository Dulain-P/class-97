introstring = input("Enter your introduction: ")
charcount = 0
wordcount = 1
for i in introstring:
    charcount = charcount + 1
    if (i==" "):
        wordcount = wordcount + 1
print(wordcount)
print(charcount)