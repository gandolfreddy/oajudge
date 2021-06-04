# need to modify the description

# input
s = input()
s = s.replace("sort_dict(", '').replace(")", '').replace("\"", '')

# process


def sort_dict(s):
    lt = s.split()
    len_lt = len(lt)
    dt = dict()
    for i in range(len_lt):
        dt[''.join(lt[i])] = sum(
            map(lambda ch: ord(ch)-96, list(lt[i].lower())))
    lt = sorted(dt.items(), key=lambda elem: elem[1])
    return [elem[0] for elem in lt]


result = sort_dict(s)

# output
print(result)
