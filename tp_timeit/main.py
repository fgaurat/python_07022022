import timeit

def list1():
    l = []
    for i in range(100):
        l.append(i)

def list2():
    l = [i for i in range(100)]

def main():
    t1 = timeit.timeit("list1()",setup="from __main__ import list1",number=10000)
    t2 = timeit.timeit("list2()",setup="from __main__ import list2",number=10000)
    print(t1)
    print(t2)


if __name__ == '__main__':
    main()