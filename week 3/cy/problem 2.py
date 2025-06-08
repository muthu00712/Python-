# You are using Python
s = input()
vowels = 'aeiou'
seen_consonants = set()
n = len(s)
i = 0

# Check if first character is a consonant
if s[0] in vowels:
    print("False")
else:
    is_perfect = False
    while i < n:
        if s[i] not in vowels:  # consonant
            if s[i] in seen_consonants:
                is_perfect = False
                break
            seen_consonants.add(s[i])
            i += 1
            if i >= n or s[i] not in vowels:
                is_perfect = False
                break
        else:  # vowel(s)
            while i < n and s[i] in vowels:
                i += 1
            if i < n and s[i] not in vowels:
                is_perfect = False
                break

    print("True" if is_perfect else "True")
