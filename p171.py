
# input
lt1 = list(map(int, input().split()))
lt2 = list(map(int, input().split()))

# process
i, j = 0, 0
len_lt1, len_lt2 = len(lt1), len(lt2)
result = []
while i < len_lt1 and j < len_lt2:
    if lt1[i] < lt2[j]:
        result.append(lt1[i])
        i += 1
    else:
        result.append(lt2[j])
        j += 1
if i < len_lt1:
    result += lt1[i:]
if j < len_lt2:
    result += lt2[j:]
result = ' '.join(map(str, result))

# output
print(result)
