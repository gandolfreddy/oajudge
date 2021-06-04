
# input
bias = int(input())
plain_lt = list(input().lower())

# process
cypher_lt = []
for ch in plain_lt:
    n_ord = ord(ch)+bias-1
    n_ord = n_ord % 122+97 if n_ord >= 122 else n_ord+1
    n_ch = chr(n_ord) if ch.islower() else ch
    cypher_lt.append(n_ch)
cypher_t = ''.join(cypher_lt)

# output
print(cypher_t)
