def fun1(a):
    print(a)

fun1(a=1)

def fun2 (a, **kwargs):
    print(a)
    print(kwargs)

fun2(10, a1=1,b=2)

def fun3(a, *args):
    print(a)
    print(args)

fun3(12, 1,3)

f = lambda a1,a2:a1+a2

print(f(1,2))

sum = 0
def f1():
    global sum
    sum = sum+1
    print(sum)

f1()

