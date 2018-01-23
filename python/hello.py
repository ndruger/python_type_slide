import typing

def f1(a: str):
    print(a)

def f2(a):
    f1(a)

print(typing.get_type_hints(f2))
f2(10)
