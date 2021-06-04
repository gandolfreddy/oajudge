
# input
lt_s = list(input())
lt_n = tuple(map(int, list(input())))

# process
len_s = len(lt_s)
len_n = len(lt_n)
if len_s > len_n:
    lt_n += lt_n[:len_s-len_n]
if len_s < len_n:
    lt_n = lt_n[:len_s]
for i in range(len_s):
    lt_s[i] = chr(ord(lt_s[i])+lt_n[i])
result = ''.join(lt_s)

# output
print(result)
