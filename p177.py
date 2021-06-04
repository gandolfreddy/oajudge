# input
pw = input()

# process
len_pw = len(pw)
dt = {"digit": False, "alphabet": False, "signs": False}
for i in range(len_pw):
    if pw[i].isnumeric():
        dt["digit"] = pw[i].isnumeric()
    elif pw[i].islower() or pw[i].isupper():
        dt["alphabet"] = True
    else:
        dt["signs"] = True
result = dt["digit"] and dt["alphabet"] and not dt["signs"]

# output
print(result)
