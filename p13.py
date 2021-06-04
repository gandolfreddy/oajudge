# input
name = input()

# process
discount = 0
if "鮭魚" in name:
    discount = 0
elif "鮭" in name and "魚" in name:
    discount = 5
elif "鮭" in name or "魚" in name:
    discount = 7
else:
    discount = 10

# output
print(discount)
