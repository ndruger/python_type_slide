
# NewType

from typing import NewType, cast, Any

TypeX = NewType('TypeX', int)

def f4(a: TypeX):
    print(a + 1)

# f4(10) # エラー。intはTypeXではない。Nominal Type。
f4(TypeX(10)) # OK
#f4(TypeX(1) + TypeX(2)) # エラー。足すとintになるのでTypeXではない


# キャスト

f4(cast(TypeX, 10)) # OK。intをTypeXにキャスト
f4(cast(Any, 10)) # OK。intをTypeXにキャスト
# f4(cast(Any, "str")) # OK(型チェックとしては)。ただし実行時にf4()内で+1されるとエラーになる。

# クラス (TODO: 継承とsuper)

# TODO: type script and flowを比較に追加。nominal/structuralな例＆subtypeの振る舞い。
# nominalならばstructuralをどう対応するかでflowはinterfaceしたけど、pythonは？
# subclass/superも比較。
# bound(TODO)もあるが、それは一旦置くか。
# structural typeの提言はあったらしいが・・・。 https://www.python.org/dev/peps/pep-0544/

class MySuperClass:
    super_name: str

class MyClass1(MySuperClass):
    name: str

class MyClass2(MySuperClass):
    name: str

class MySubClass(MyClass1):
    sub_name: str

def fx(a: MyClass1):
    print(a)

fx(MyClass1()) # OK
# fx(MyClass2()) # NG。クラスの型チェックはNominal Type
# fx(MySuperClass()) # NG。superはだめ
fx(MySubClass()) # OK。subはOK

o = MyClass1()
# o.name = 2 # NG
# o.missing_method() # NG

# NewTypeをしない場合はStructual Typeなのか？

TypeA = List[str]
TypeB = List[str]

def f5(a: TypeA):
    f6(a)

def f6(a: TypeA):
    print(a)

f5(["s"])

s = ["s"] # type: TypeB
f5(s)

# Unicon(TODO)

# Generics(TODO)

# TypeVar(TODO)


# 途中に未定義を挟んだ場合

# flowでの$diffと$elementを使って

# anyは何がanyなのか。flowのmixedとの比較
