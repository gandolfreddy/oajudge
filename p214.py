
# input & process
n = int(input())
a_ii = list(map(int, input().split()))
for i in range(n-1):
    b_ii = list(map(int, input().split()))
    a_ii = [a_ii[0]*b_ii[0]+a_ii[1]*b_ii[2],
            a_ii[0]*b_ii[1]+a_ii[1]*b_ii[3],
            a_ii[2]*b_ii[0]+a_ii[3]*b_ii[2],
            a_ii[2]*b_ii[1]+a_ii[3]*b_ii[3]]

# output
print(a_ii)
