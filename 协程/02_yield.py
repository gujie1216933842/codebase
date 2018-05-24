def fun(a):
    b = 0
    while a > 1:
        a -= 1
        b = yield a
        yield b
    return b

bb = fun(5)

print(next(bb))
print(bb.send('hhhhh'))

print(next(bb))
