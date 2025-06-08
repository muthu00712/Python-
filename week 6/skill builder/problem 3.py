sentence = input()
with open("sentence_file.txt", "w") as f:
    f.write(sentence)

with open("sentence_file.txt", "r") as f:
    content = f.read()

words = content.split()
print(len(words))

