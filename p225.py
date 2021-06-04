
# input
s = input()

# process
new_s = s
for ch in s:
    if not (ch.isalpha() or ch.isspace()):
        new_s = new_s.replace(ch, '')
cnt_w = len(new_s.split())
cnt_ch = len(new_s.replace(' ', ''))

# output
print(cnt_w)
print(cnt_ch)
