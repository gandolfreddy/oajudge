# input & process
names = ['Ni', 'On', 'Sa', 'Ai', 'Ma', 'Fu', 'Sk',
         'Wa', 'Mi',  'I',  'A', 'Mu', 'Me', 'Ra',
         'Je', 'Ky', 'Mt', 'Ko', 'Ta', 'Mo']
colors = ['red',  'pink', 'black', 'yellow',  'blue',  'green', 'purple',
          'pink',  'blue',   'red', 'yellow', 'green', 'orange',  'black',
          'white', 'yellow', 'blue',    'red', 'green', 'purple']


def ten_color(name_lst, color_lst):
    len_name = len(name_lst)
    n_c_dt = {name_lst[i]: color_lst[i] for i in range(len_name)}
    color_in_lst = []
    while True:
        color = input()
        if not color in color_lst:
            break
        color_in_lst.append(color)
    name_out_lst = []
    for color in color_in_lst:
        name_out_lst += list(filter(lambda item: item[1]
                                    == color, n_c_dt.items()))
    return [item[0] for item in name_out_lst]


result = ten_color(names, colors)

# output
print(result)
