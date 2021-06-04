# input
n = int(input())
materials = input().split()
len_m = len(materials)
materials_dt = {materials[i]: int(materials[i+1]) for i in range(0, len_m, 2)}

n = int(input())
menu_dt = {}
for i in range(n):
    dish = input().split()
    len_d = len(dish[1:])
    menu_dt[dish[0]] = tuple((dish[i], int(dish[i+1]))
                             for i in range(1, len_d, 2))

n = int(input())
wish_lt = [input() for i in range(n)]

# process & output
for wish in wish_lt:
    if wish in menu_dt:
        for item in menu_dt[wish]:
            enough = False
            if item[0] in materials_dt and item[1] <= materials_dt[item[0]]:
                materials_dt[item[0]] -= item[1]
                enough = True
            else:
                enough = False
                break
    print(enough)
