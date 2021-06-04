from math import ceil

# input
x = int(input())  # total
m = int(input())  # chocolate
n = int(input())  # strawberry
y = x - m - n    # choco & berry

# process
powder_amount = ceil((90*m + 50*n+120*y)/220)
powder_cost = powder_amount * 50
egg_amount = ceil((3*m+2*n+4*y)/8)
egg_cost = egg_amount * 76
coco_amount = ceil((0.5*m+1.25*y)/1)
coco_cost = coco_amount * 300
berry_amount = 10*n + 6*y
berry_cost = berry_amount//10*25 + berry_amount % 10*3

total_cost = powder_cost + egg_cost + coco_cost + berry_cost

# output
print(f"{total_cost},{egg_amount}")
