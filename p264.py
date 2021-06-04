import re

# input
label = input()
datas = []
while True:
    data = input()
    if data == "raw-data.txt":
        break
    data = data.split('\t')
    datas.append(data)

raw_datas = []
while True:
    try:
        raw_data = input()
        raw_datas.append(raw_data)
    except:
        break

# process
regex = re.compile("[a-z]")
re_datas = []
for data in datas:
    re_datas.append(regex.findall(data[1]))

re_raw_datas = []
for data in raw_datas:
    re_raw_datas.append(regex.findall(data.lower()))

for i, data in enumerate(re_raw_datas):
    if data in re_datas:
        datas[re_datas.index(data)][1] = raw_datas[i]

datas = ['\t'.join(data) for data in datas]

# output
for data in datas:
    print(data)
