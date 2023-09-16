# Python New Features
l = [10, 20, 30, 40, 50]

if (n := len(l)) > 3:
    print("List contain 3 elements")
    print('The Lenght of the list', n)

print(n)

heroines = []

# print(type(heroines))

while (heroine := input("Enter your Favouritte actress")) != 'done':
    heroines.append(heroine)
print(heroines)


