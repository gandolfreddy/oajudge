from math import ceil

# input
in_parking = tuple(map(int, input().split(':')))
out_parking = tuple(map(int, input().split(':')))
have_ID = input()

# process
total_t = (out_parking[0]*60+out_parking[1]) - (in_parking[0]*60+in_parking[1])
if have_ID == 'Y':
    charge = ceil(total_t/30) * 10
else:
    charge = ceil(total_t/30) * 20

# output
print(charge)
