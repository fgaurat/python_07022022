from collections import deque


values = [1,2]
values.append(3)
print(values)
i = values.pop()
print(i)
print(values)

d = deque(values)

d.appendleft(0)
# d.popleft(0)
d.append(3)
print(d)
print(type(d))


# result = deque(map(lambda i:i*2, d))
# print(result)

print(50*'-')
# result2 = []

# for v in d:
#     result2.append(v*2)
    
# print(result2)
result2 = [v*2 for v in d]
print(result2)

l = [' toto  ','tutu ', '   tata','tete  ']
list1 = []

for v in l:
    list1.append(v.strip())

print(list1)
# list1 = [ ''.join([i for i in v if i != ' ']) for v in l]
list1 = [ v.strip() for v in l]
print(list1)


l3 = [i for i in range(30) if i%2 == 0]
print(l3)

print(50*'-')

label = ['name','firstname','age']
values= ['GAURAT','Frédéric',45]

data = [label,values]

# r = list(zip(label,values))
r = list(zip(*data))
print(r)

print(50*'-')

a = 2
print(a)


label = ['name','firstname','age']
print(label)
del label[0]
print(label)