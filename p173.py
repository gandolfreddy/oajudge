# Can not use module numpy

# input
text1 = input().split('|')
text2 = input().split('|')

# process
st = set(text1) | set(text2)
vec_t1 = tuple(text1.count(elem) for elem in st)
vec_t2 = tuple(text2.count(elem) for elem in st)
dot_t1_t2 = 0
len_st = len(st)
for i in range(len_st):
    dot_t1_t2 += vec_t1[i]*vec_t2[i]
len_vec_t1 = sum(map(lambda x: x**2, vec_t1))**0.5
len_vec_t2 = sum(map(lambda x: x**2, vec_t2))**0.5
result = dot_t1_t2 / (len_vec_t1*len_vec_t2)

# output
print(result)
