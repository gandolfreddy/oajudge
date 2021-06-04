
# input
card1 = input().split()
card2 = input().split()
r1, r1_atk, r1_hp = card1[0], int(card1[1]), int(card1[2])
r2, r2_atk, r2_hp = card2[0], int(card2[1]), int(card2[2])

# process
while r1_hp > 0 and r2_hp > 0:
    r1_hp -= r2_atk
    r2_hp -= r1_atk
winner = None
if r1_hp > 0:
    winner = ' '.join([r1, str(r1_atk), str(r1_hp)])
elif r2_hp > 0:
    winner = ' '.join([r2, str(r2_atk), str(r2_hp)])
else:
    winner = "tie"

# output
print(winner)
