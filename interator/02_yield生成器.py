def fun():
    for i in range(10):
        yield i


a = fun()
print(next(a))
print(next(a))
print(next(a))
print(next(a))