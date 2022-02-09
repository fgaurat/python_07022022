# List
squares = [1, 4, 9, 16, 25]

print(squares)
print(squares[0])
print(squares[-1])
print(squares[:-3])
print(squares[-3:-1])
print(squares[-3:])
print(id(squares))
print(id(squares[:]))


s2 = squares[:]

squares[0] = 1000
print(squares)
print(s2)

print(50*'-')
l2 = [
    [10,20],
    [30,40],
    [50,60]
]
print(l2)
print(l2[1][1])
l3 = l2[:]
l2[1][1] = 4000
print(l2)
print(l3)
l2[-1] = [70,80]
print(50*'-')
print(l2)
print(l3)
print(50*'-')
l1 = [10,20,30]
l2 = [40,50,60]
l3 = l1+l2
print(id(l1))
print(id(l2))
print(id(l3))


# l3[1] = 65
# print(l1)
# print(l2)
# print(l3)

l2 = [
    [10,20],
    [30,40],
    [50,60]
]
l1 = l2+[]
print(id(l2))
print(id(l1))
l2[1][1] = 4000
print(l2)
print(l1)

l1 = [10,20,30]
print(l1)
l1.append(40)
l1.insert(1,40)
print(l1)