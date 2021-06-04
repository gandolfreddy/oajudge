x, y = list(map(int, input().split()))

result = None
if x == 0 and y == 0:
    result = '0'
elif x == 0:
    result = 'y'
elif y == 0:
    result = 'x'
elif x > 0 and y > 0:
    result = '1'
elif x < 0 and y > 0:
    result = '2'
elif x < 0 and y < 0:
    result = '3'
elif x > 0 and y < 0:
    result = '4'

print(result)
