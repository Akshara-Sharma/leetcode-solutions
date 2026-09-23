s = "abcd"
t = "abcde"

s = sorted(s)
t = sorted(t)

for i in range(len(s)):
    if s[i] != t[i]:
        print(t[i])
        break
else:
    print(t[-1])