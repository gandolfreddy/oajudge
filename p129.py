
# input
s = input()

# process
dt = {chr(ord('a')+i): 0 for i in range(26)}
s = s.lower()
for ch in s:
    if ch in dt:
        dt[ch] += 1
lt = [f"{ch}{cnt}" for ch, cnt in dt.items() if cnt]
result = ' '.join(lt)

# output
print(result)
