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
         next(self.generator)

F = Fibonacci(100)
x = F.generator(10)
print(F.lst_fib)

class TestInit:

    def test_gen1(self):
        assert(next(x)==0)

    def test_gen2(self):
        assert(next(x)==1)

    def test_gen3(self):
        assert(next(x)==1)

    def test_gen4(self):
        assert(next(x)==2)

    def test_gen5(self):
        assert(next(x)==3)

    def test_gen6(self):
        assert(next(x)==5)

    def test_gen7(self):
        assert(next(x)==8)

