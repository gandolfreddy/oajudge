# need to modify the description that says there's no need in input but it needs input actually

# input
s = input()
s = s.replace("calculator(", '').replace(")", '').replace("\"", '')
n1, n2, op = s.split(", ")

# process


def calculator(num1, num2, op):
    ans = float(eval(n1+op+n2))
    return ans


result = calculator(n1, n2, op)

# output
print(result)
