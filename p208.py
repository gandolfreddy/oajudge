from random import randint, seed


# input
rand_seed, n = list(map(int, input().split()))
seed(rand_seed)
a = randint(1, 1000000000)
b = randint(1, 1000000000)
c = randint(1, 10000)

# process & output
for i in range(n):
    rand_seed = (a*rand_seed+b) % c
    seed(rand_seed)
    print(rand_seed)
