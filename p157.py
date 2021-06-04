
# input
ids = input().split()

# process


def mulit_sort(idn):
    return tuple(idn[:3])


collage = {"902": 2, "901": 1}
grade = {"04": 1}
ids_precedence = []
for idn in ids:
    seg1, seg2, seg3 = idn[3:6], idn[1:3], int(idn[-3:])
    idn_precedence = (
        collage[seg1] if seg1 in collage else 0,
        grade[seg2] if seg2 in grade else 0,
        1 if not (seg3 % 3 and seg3 % 5 and seg3 % 7) else 0,
        idn,
    )
    ids_precedence.append(idn_precedence)

result = sorted(ids_precedence, key=mulit_sort, reverse=True)

# output
for item in result:
    print(item[3])
