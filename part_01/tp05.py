# Function

def fib(n):    # write Fibonparam_valuecci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()



def fib2(toto=10) ->list:
    """Return a list with Fibonacci series"""
    a,b=0,1
    result = []
    while a < toto:
        result.append(a)
        a, b = b, a+b
    return result    


# fib(100)
# f = fib2(2000)

# print(f) # [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597 ]
# # Now call the function we just defined:

# print( type(fib))
# toto =fib
# toto(12)
# print("fin")


a = fib2()
print(a)

print(50*'-')


param_value=12
def f(p=param_value):
    print(p)

param_value=1
f()

def f2(a,p=[]):
    p.append(a)
    return p

def f3(a,p=None):
    if p== None:
        p = []
    p.append(a)
    return p

l1 = f2(1) # [1]
print(l1)
l2 = f2(2) # [1,2]
print(l2)
l3 = f2(3)# [1,2,3]
print(l3)

l1 = f3(1) # [1]
print(l1)
l2 = f3(2) # [2]
print(l2)
l3 = f3(3)# [3]
print(l3)