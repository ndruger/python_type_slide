from typing import Any

x: Any = 'text'
x = 10

z: bool = True
z = x # OK。Anyが持つ値を他の型にも入れることができてしまう。
