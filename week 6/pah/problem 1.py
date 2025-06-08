flename = input()
content = input()
char_to_count = input()
with open(flename, 'w') as fle:
 fle.write(content)
with open(flename, 'r') as fle:
 data = fle.read()
 count = data.lower().count(char_to_count.lower())
if count > 0:
 print(f"The character '{char_to_count}' appears {count} times in the fle.")
else:
 print("Character not found in the fle.")