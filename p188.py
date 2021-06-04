# indentation before "return" in example is wrong

# input
s = input()
s = s.replace("char_puzzle([", '').replace("])", '').replace("\"", '').replace(",", '')
lst = s.split()

# process
def char_puzzle(lst):
    ans = ''.join(sorted(list(set(''.join(lst)))))
    return ans
result = char_puzzle(lst)
  
# output
print(result)