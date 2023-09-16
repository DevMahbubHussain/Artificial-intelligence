l = list(range(0, 10, 2))
print(l)

sp = 'Learning pyrthon is very very easy'
l = sp.split()
print(l)

ll = [1, 20, 3, 5, 8, 8, 9]

for i in ll:
    if i % 2 == 0:
        print(i)

i = 0
while i < len(ll):
    print(ll[i])
    i = i + 1

ls = ['A', 'B', 'C', 'D']
data = len(ls)
for i in range(data):
    print(ls[i], "is avilable at positive index:", i, "and negative index : ", i - data)

a = [10, 20, 30, 40]
b = [20, 50, 60, 60]
c = a + b
print(len(c))

la = [10, 20, 60, 10, 20]

print(la.count(100))
