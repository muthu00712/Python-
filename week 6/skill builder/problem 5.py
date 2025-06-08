text = input()

with open("text_file.txt", "w") as f:
    f.write(text)

with open("text_file.txt", "r") as f:
    original = f.read()

print(f"Original String: {original}")
print(f"Upper-Case String: {original.upper()}")
print(f"Lower-Case String: {original.lower()}")

