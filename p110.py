
# input
score = int(input())

# process
result = ""
if score < 0 or score > 100:
    result = "Error"
elif score >= 60:
    result = "Pass"
else:
    result = "Fail"

# output
print(result)
