# the description needs modifying

# input
plain_txt = input()
key_txt = input()

# process
alphas_order = [chr(ord('a')+i) for i in range(26)]


def encrypt(plain, key, idx):
    len_k = len(key)
    cypher_ch = alphas_order[(alphas_order.index(plain[idx])+1 +
                              alphas_order.index(key[idx % len_k])+1 +
                              alphas_order.index(key[(idx+1) % len_k])+1)-1]
    return cypher_ch


cypher_txt = ''
len_p = len(plain_txt)
for i in range(len_p):
    cypher_txt += encrypt(plain_txt, key_txt, i)

# output
print(cypher_txt)
