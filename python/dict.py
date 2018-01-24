
# NewType

from typing import NewType, cast, Any

TypeX = NewType('TypeX', int)

def f4(a: TypeX):
    print(a + 1)

# f4(10) # NG。intはTypeXではない。Nominal Type。
f4(TypeX(10)) # OK
#f4(TypeX(1) + TypeX(2)) # NG。足すとintになるのでTypeXではない


# クラス (TODO: 継承とsuper)

# TODO: type script and flowを比較に追加。nominal/structuralな例＆subtypeの振る舞い。
# nominalならばstructuralをどう対応するかでflowはinterfaceしたけど、pythonは？
# subclass/superも比較。
# bound(TODO)もあるが、それは一旦置くか。
# structural typeの提言はあったらしいが・・・。 https://www.python.org/dev/peps/pep-0544/



# Generics(TODO)

# TypeVar(TODO)


# 途中に未定義を挟んだ場合

# flowでの$diffと$elementを使って

# anyは何がanyなのか。flowのmixedとの比較
