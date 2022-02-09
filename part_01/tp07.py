# Lambda

def mult2(i):
    return i*2

values = [1,2,3,4]
result = []

for value in values:
    v = value*2
    result.append(v)

print(result) # [2,4,6,8]

# result = map(mult2,values)
result = map(lambda i:i*2, values)
result = list(result)
print(result)