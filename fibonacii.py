import  sys

def fibonacii(n):

    a, b, count= 0, 1, 0
    while True:
        if (count > n):
            return
        yield a
        a, b = b, a+b
        count += 1

f = fibonacii(10)

while True:
    try:
        print(next(f), end=' ')
    except StopAsyncIteration:
        sys.exit()

