def f(a: str) -> bool:
    print('Hello ' + a)
    return True

# f(10) # NG。10がstrではない。
f('Python') # OK
