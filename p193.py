
# input
s = input()

# process
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
start, end = -1, -1
len_s = len(s)
for i in range(len_s):
    if s[i] in vowels:
        start = i
        break
for i in range(len_s-1, start-1, -1):
    if s[i] in vowels:
        end = i
        break
vowel_s = s[start:end+1] if start != -1 and end != -1 else ''

# output
print(vowel_s)
