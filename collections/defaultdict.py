from collections import defaultdict

#get first line
n_m = input()
n_m_list = [int(x) for x in n_m.split()]
n = n_m_list[0]
m = n_m_list[1]

#create the defaultdict
d = defaultdict(list)

# get second line and create group  A
for element in range(n):
    A = input()
    d['A'].append(A)
for element in range(m):
    B = input()
    d['B'].append(B)

for element in d['B']:
    if element in d['A']:
        e = [pos+1 for pos,val in enumerate(d['A']) if val == element]
        print(e)
        print(*e, sep=' ')
    else:
        print(-1)
