# picture is disable, resource: http://www.bebi.ntu.edu.tw/uploads/root/Regulations.pdf

# input
score = int(input())

# process
level = ''
if score <= 100 and score >= 90:
    level = "A+"
elif score <= 89 and score >= 85:
    level = "A"
elif score <= 84 and score >= 80:
    level = "A-"
elif score <= 79 and score >= 77:
    level = "B+"
elif score <= 76 and score >= 73:
    level = "B"
elif score <= 72 and score >= 70:
    level = "B-"
elif score <= 69 and score >= 67:
    level = "C+"
elif score <= 66 and score >= 63:
    level = "C"
elif score <= 62 and score >= 60:
    level = "C-"
elif score <= 59 and score >= 1:
    level = "F"
else:
    level = "X"

# output
print(level)
