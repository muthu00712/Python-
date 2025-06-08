def compress_string(s):
    result = ''
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        if count > 1:
            result += s[i] + str(count)
        else:
            result += s[i]
        i += 1
    return result
   
    print(result)

s=input()
d=compress_string(s)
print(d)


