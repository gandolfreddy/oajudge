
# input
lt = list(input())

# process
len_lt = len(lt)
for i in range(len_lt):
    lt[i] = chr(ord(lt[i])+i+1)
s = ''.join(lt)

# output
print(s)
