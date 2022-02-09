def hello(name="",firstname="",age=45):
    print("hello",name,firstname,age)



hello("GAURAT","Fred")
hello(firstname="Fred",name="GAURAT")

hello()
hello("GAURAT",firstname="Fred")
# hello(name="GAURAT",'Fred')
hello("GAURAT","Fred",age=45)

print(50*'-')


def add_all(*values)->int:
    print(values) # (1,2,3) = t-uple
    somme = 0
    for i in values:
        somme+=i # somme = somme+i
    return somme


v= [1,2,3,4,5]
print([1,2,3])
result = add_all(1,2,3)
print(result) # 15

print('toto','tutu','12345')

def hello2(**values):
    print(values ) # {'name':'toto'}
    print(values['name']) 
    # print(values)

def hello3(*pos, **values):
    print(values ) # {'name':'toto'}
    print(values['name']) 
    # print(values)
    

hello2(name="toto")
hello2(name="toto",firstname="titi",age=45)
hello3(1,2,3,545,name="toto",firstname="titi",age=45)


def somme(*,a,b):
    return a+b

# c = somme(1,2)
# print("par position",c)
c = somme(a=1,b=2)
print("par keywords",c)

print(50*'-')



values = [1,2,3]
print(values)
print(*values)
somme = add_all(*values)


