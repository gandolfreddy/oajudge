
# input
id1 = input()
id2 = input()

# process
collage = {"902": 2, "901": 1}
grade = {"04": 1}
seg1, seg2, seg3 = id1[3:6], id1[1:3], int(id1[-3:])
id1_precedence = (
    collage[seg1] if seg1 in collage else 0,
    grade[seg2] if seg2 in grade else 0,
    1 if not (seg3 % 3 and seg3 % 5 and seg3 % 7) else 0
)
seg1, seg2, seg3 = id2[3:6], id2[1:3], int(id2[-3:])
id2_precedence = (
    collage[seg1] if seg1 in collage else 0,
    grade[seg2] if seg2 in grade else 0,
    1 if not (seg3 % 3 and seg3 % 5 and seg3 % 7) else 0
)

if id1_precedence[0] > id2_precedence[0] or id1_precedence[1] > id2_precedence[1] or id1_precedence[2] > id2_precedence[2]:
    pri = id1
elif id1_precedence[0] < id2_precedence[0] or id1_precedence[1] < id2_precedence[1] or id1_precedence[2] < id2_precedence[2]:
    pri = id2
else:
    pri = "tie"

# output
print(pri)
