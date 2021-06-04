# the picture is invisiable


# input
scores = list(map(int, input().split(',')))
ta = input()

# process
is_passed = 0
mad, eng, math, social, sci = scores
if ta == "會計系":
    if mad+eng+math+social == 57 and mad == 15:
        is_passed = 1
elif ta == "公衛系":
    if eng+math+sci == 38:
        is_passed = 1
elif ta == "經濟系":
    if social+sci == 26 and math == 15:
        is_passed = 1
elif ta == "資工系":
    if eng+sci == 27 and math == 15:
        is_passed = 1

# output
print(is_passed)
