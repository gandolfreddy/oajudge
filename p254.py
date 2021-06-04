# the description needs modifying

# input
face_lt = input().split()

# process & output
num_dt = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
          "六": 6, "七": 7, "八": 8, "九": 9}
type_dt = {"筒": 1, "條": 10, "萬": 100}
char_dt = {"東風": 901, "南風": 902, "西風": 903, "北風": 904,
           "紅中": 905, "發財": 906, "白板": 907}
all_dt = {}
for n_k, n_v in num_dt.items():
    for t_k, t_v in type_dt.items():
        all_dt[f"{n_k}{t_k}"] = n_v * t_v
all_dt.update(char_dt)

res_lt = []
for face in face_lt:
    res_lt.append(face)
    i = len(res_lt) - 1
    print(' '.join(res_lt))
    while i and all_dt[res_lt[i]] < all_dt[res_lt[i-1]]:
        res_lt[i], res_lt[i-1] = res_lt[i-1], res_lt[i]
        i -= 1
        print(' '.join(res_lt))
