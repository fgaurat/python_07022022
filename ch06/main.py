import fibo as fibo_module
from fibo import fib as the_fib
import sys

import calc_math.calc
from calc_math import calc
from calc_math.calc import somme

def fib(n):
    print('je suis fib',n) 


def main(val):
    fibo_module.fib(val)
    print("module name",__name__)
    the_fib(val)
    a = calc_math.calc.somme(1,2)
    a = calc.somme(1,2)
    print(a)

if __name__=='__main__':
    val = int(sys.argv[1])    
    main(val)

