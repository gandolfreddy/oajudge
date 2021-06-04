lower_vowels = ('a', 'e', 'i', 'o', 'u')
upper_vowels = ('A', 'E', 'I', 'O', 'U')

# input
s = input()

# process
cnt = 0
for vowel in lower_vowels:
    if vowel in s:
        cnt += 1

for vowel in upper_vowels:
    if vowel in s:
        cnt += 1

# output
print(cnt)
