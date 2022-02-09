# Tuple

def f():
    
    return 0,1


a,b = f()


a = 0,


a,b = 0,1

def somme(a,*values):
    print(values)
    a,b,*p = values

a,b,*p = 0,1,2,3
# a,b,*p = 0,1,2,3
# *a,b,p = 0,1,2,3

# print(a,b,p)



result = somme(1,2,3,4)


the_list = ["value 01","value 02","value 03"]

for i,value in enumerate(the_list):
    print(value)

if "value 01" in the_list:
    print('ok')



the_set = {"value 01","value 02","value 03"}
if "value 01" in the_set:
    print('ok')

