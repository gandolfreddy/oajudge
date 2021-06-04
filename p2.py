h, w = list(map(int, input().split()))

bmi = w / ((h/100)**2)
result = None
if bmi < 18.5:
    result = "underweight"
elif bmi >= 18.5 and bmi <= 25:
    result = "normal"
else:
    result = "overweight"

print(result)
