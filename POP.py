# pop function

# l = [10,20,30]
# l.clear()
# print(l)

# print(l.pop(2))
# print(l)
# print(l.pop())
# print(l)


# l = [10, 20, 30, 40, 0]
# l2 = sorted(l)
# print(l2)
# print(l)
# l.sort(reverse=True)
# print(l)


# l.sort()
# print(l)
# r = reversed(l)
# l1 = list(r)
# print(l1)
# print(l)
# l.reverse()
# print(l)


# name = 'Mahbub Hussain'
# t = reversed(name)
# for x in t:
#     print(x)


#  Cloning
l = [10,20,30,40]
l1 = l[::]
print(id(l))
print(id(l1))
print(l is l1)

l1[1] = 777
l[1] = 999
print(l)
print(l1)