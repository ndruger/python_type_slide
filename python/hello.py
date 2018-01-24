from typing import NewType, cast, Any

TypeX = NewType('TypeX', int)

def f4(a: TypeX):
    print(a + 1)

f4(10) # NG。intはTypeXではない。Nominal Typingなのでエラーになる。
# f4(TypeX(10)) # OK
