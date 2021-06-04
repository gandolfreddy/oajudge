
# input
iron_b = int(input())
bat_b = int(input())
total_s = int(input())
total_b = int(input())

# process
bat_s = (iron_b*total_s-total_b)/(iron_b-bat_b)
iron_s = total_s - bat_s

res = bat_s > 0 and iron_s > 0 and \
    bat_s.is_integer() and iron_s.is_integer()

# output
print(res)
