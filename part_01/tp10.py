

# json : JavaScript Object Notation

d ={ 
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
}

print(d['id'])
print(d['title'])

print(list(d))
d['completed'] = True

d['name'] = 'GAURAT'
print(d)




print(d.keys())
for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key,value in d.items():
    print(key,value)