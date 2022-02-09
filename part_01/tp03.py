# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a,end=",")
    a, b = b, a+b
print()


print(1,2,3,4,5,6,sep=" - ")

r:str=" "
print("start",id(r))
for i in range(20):
    # print(r+"\t"+str(id(r)))
    print(id(r))
    r = r + str(i)

# print(50*'-')
# r=""
# print(r,'\t',id(r))
# r=r+"0"
# print(r,'\t',id(r))
# r=r+"1"
# print(r,'\t',id(r))
# r=r+"2"
# print(r,'\t',id(r))
# r=r+"3"
# print(r,'\t',id(r))
# r=r+"4"
# print(r,'\t',id(r))

