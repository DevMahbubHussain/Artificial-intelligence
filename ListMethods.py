# index


l = []

for i in range(101):
    if i % 10 == 0:
        l.append(i)
print(l)

n = [1, 2, 2, 2, 2, 3, 3]

x = int(input("Enter element to search"))
if x in n:
    print('{} present at index: {}'.format(x, n.index(2)))
else:
    print(x, 'not in list')

order1 = ['chicken', 'Mutton', 'Fish']
order2 = ['RC', 'KF', 'FO']
order1.extend(order2)
print(order1)
