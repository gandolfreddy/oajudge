# need to modify the description about input

# input
op = input()

# process


def parking_fee(fee_rate, is_vip, entry_time, exit_time):
    from math import ceil

    fee_rate = int(fee_rate)
    have_ID = bool(is_vip)
    in_t = tuple(map(int, entry_time.split(':')))
    out_t = tuple(map(int, exit_time.split(':')))

    total_t = (out_t[0]*60+out_t[1]) - (in_t[0]*60+in_t[1])
    if have_ID:
        charge = ceil(total_t/30) * fee_rate//2
    else:
        charge = ceil(total_t/30) * fee_rate
    return charge


op = op.replace("parking_fee(", '').replace(")", '')\
       .replace("\"", '').replace(",", '').split()

# output
print(parking_fee(op[0], op[1], op[2], op[3]))
