
# input
ch = input()
lt_n = list(input())

# process
dt = {'A': '10', 'B': '11', 'C': '12', 'D': '13',
      'E': '14', 'F': '15', 'G': '16', 'H': '17',
      'I': '34', 'J': '18', 'K': '19', 'L': '20',
      'M': '21', 'N': '22', 'O': '35', 'P': '23',
      'Q': '24', 'R': '25', 'S': '26', 'T': '27',
      'U': '28', 'V': '29', 'W': '32', 'X': '30',
      'Y': '31', 'Z': '33', }


def is_right_gender(gender):
    n1, n2 = dt[ch]
    check_sum = int(n1)*1 + int(n2)*9 + \
        gender*8 + int(lt_n[-1])*1
    for i in range(7):
        check_sum += int(lt_n[i]) * (7-i)
    return not check_sum % 10


if is_right_gender(1):
    result = "Male"
if is_right_gender(2):
    result = "Female"

# output
print(result)
