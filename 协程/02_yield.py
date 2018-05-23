def fun(a):
    b = 0
    while a > 1:
        a -= 1
        b = yield a
    return b

bb = fun(5)

print(next(bb))
print(next(bb))
print(bb.send(3))

print(next(bb))
