class Fibonacci:
    def __init__(self,n):
        self.lst_fib = (lambda n, fib=[0,1]: fib[:n]+[fib.append(fib[-1] + fib[-2]) or fib[-1] for i in range(n-len(fib))])(n)

    def generator(self,n):
        fib1, fib2 = 0, 1
        yield fib1
        for i in range(n):
            fib1, fib2 = fib2, fib1 + fib2
            yield fib1

    def next(self):
        self.generator.next()

F = Fibonacci(100)
x = F.generator(10)
print(F.lst_fib)
print(list(F.generator(100)))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
