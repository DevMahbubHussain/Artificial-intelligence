# l = []
# # for i in range(1,11):
#     l.append(i)
# print(l)

# l = [x*x for x in range(1, 11)]
# print(l)
# m = [x for x in l if x % 2 == 0]
# print(m)
#  print(l)

l = [i for i in range(1, 101) if i % 10 == 0]
print(l)

l1 = [10, 20, 30, 40]
l2 = [30, 40, 50, 60]

l3 = [x for x in l1 if x not in l2]
print(l3)
l4 = [x for x in l1 if x in l2]
print(l4)
