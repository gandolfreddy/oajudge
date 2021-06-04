# the sample input 1 is in a wrong form

# input & process
n = int(input())
m = int(input())
a_ii = list(map(int, input().split()))
for _ in range(n-1):
    b_ii = list(map(int, input().split()))
    len_mat = m * m
    m_ii = [0 for i in range(len_mat)]
    for i in range(len_mat):
        k = m * (i//m)
        bias = m * (i % m)
        for j in range(bias, m+bias):
            m_ii[k] += a_ii[i] * b_ii[j]
            k += 1
    a_ii = m_ii

# output
print(m_ii)
