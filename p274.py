# the picture is invisiable

# input
hw_scores = list(map(int, input().split()))
mid_scores = list(map(int, input().split()))
final_scores = int(input())

# process
min_score = min(hw_scores)
hw_scores.remove(min_score)
hw_score = sum(hw_scores)/5
hw_score = hw_score*50/100 if hw_score < 100 else 50

mid_scores = list(map(lambda score: score if score < 100 else 100, mid_scores))
mid_score = max(mid_scores)*15/100 + min(mid_scores)*10/100
final_score = final_scores * 25/100

total = round(hw_score+mid_score+final_score)

levels = ("A+", 'A', "A-", "B+", 'B', "B-",
          "C+", 'C', "C-", 'F', 'X')
level = ''
if total >= 90 and total <= 100:
    level = "A+"
elif total >= 85 and total <= 89:
    level = 'A'
elif total >= 80 and total <= 84:
    level = "A-"
elif total >= 77 and total <= 79:
    level = "B+"
elif total >= 73 and total <= 76:
    level = 'B'
elif total >= 70 and total <= 72:
    level = "B-"
elif total >= 67 and total <= 69:
    level = "C+"
elif total >= 63 and total <= 66:
    level = 'C'
elif total >= 60 and total <= 62:
    level = "C-"
elif total < 60:
    level = 'F'
else:
    level = 'X'

if -1 == min_score:
    level = levels[levels.index(level)+2]

# output
print(f"{total} {level}")
