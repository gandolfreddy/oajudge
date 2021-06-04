# description needs modifying.(it needs "input()" to get the inputs)

def odd_even_count_sub(nums):
    #start your code here for odd_even_count_sub
    diff = 0
    for num in nums:
        diff = diff+1 if num % 2 else diff-1
    diff = abs(diff)
    return diff


def top2_max_sub(nums):
    #start your code here for top2_max_sub
    first = max(nums)
    nums.remove(first)
    second = max(nums)
    diff = first - second
    return diff


def max_odd_even_sub(nums):
    #start your code here for max_odd_even_sub
    diff = 0
    max_odd = -10000000
    max_even = -10000000
    for num in nums:
        if num % 2:
            if num > max_odd:
                max_odd = num
        else:
            if num > max_even:
                max_even = num
    diff = abs(max_odd-max_even)
    return diff


# input
nums = list(map(int, input().split()))
func_name = input()

# process
if func_name == "odd_even_count_sub":
    result = odd_even_count_sub(nums)
elif func_name == "top2_max_sub":
    result = top2_max_sub(nums)
else:
    result = max_odd_even_sub(nums)

# output
print(result)
