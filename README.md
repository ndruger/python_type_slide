# Python Type Hints

Python Type Hintsのmypyの動作を他の後付け静的型チェックと比較して見ていく。

## 例

関数の引数と戻り値の型を指定

```python
def f(a: str) -> bool:
    print('Hello ' + a)
    return True

# f(10) # エラー。10がstrではない。
f('Python') # OK
```

### flowの構文との比較

```javascript
function f(a: string): boolean {
  console.log('Hello ' + a);
  return true;
}

// f(10); // エラー。10がstringではない。
f('JavaScript');

```

## 変数の定義時に型を指定する

```python
# Python 3.5以前は、コメントで型指定。
s = 10 # type: int
# s = 'text' # type: int # エラー。この場合型と値('text')が合わない。


# Python 3.6ならコメントではない記法で型指定できる
s2: int = 10
```

## List

```python
from typing import List

def f1(a: List[float]):
    print(a)

#f1(['a']) # エラー。要素がfloatではない。
f1([10.0]) # OK
```

## Alias

型に別名を付けることができる。

```python
from typing import List

TypedList = List[float]

def f1(a: TypedList):
    print(a)
```

## Tuple

```python
from typing import Tuple

def f(a: Tuple[str, str, int]):
    print(a)

#f(('a', 'b', 'c')) # エラー。3番目ばintではない。
f(('a', 'b', 1)) # OK
```

## Dict

```python
from typing import Dict

def f(a: Dict[str, str]):
    print(a)

#f({'name': 10}) # エラー。10がstrではない。
f({'name': 'value'}) # OK
```

Dictのフィールドごとの型指定はできない。[issue](https://github.com/python/typing/issues/28)で議論はされている。

[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)ならばフィールド毎の型指定が可能。DictとNamedTupleはそもそも使い方が大分違うが、フィールドが限定されているならばNamedTupleを使えという方向なんだろうか？

### flowとの比較

flowはobjectに対するフィールドごとの型指定ができる。

```javascript
function f(a: {name: string, age: number}) {
  console.log(a)
}

// f({name: 10, age: 10}) // エラー。10がstringではない。
f({name: 'Bob', age: 10}) // OK

```

## 引数の型を未指定の関数を経由した場合

引数の型指定のないf2を経由したら、型のミスマッチのエラーが起きなくなる。これがPython Type Hintsの仕様なのかmypyの実装による挙動なのかは不明。

```python
def f1(a: str):
    print(a)

def f2(a):
    f1(a)

f2(10) # エラーにならない。
```

### flowとの比較

flowは相当コードを見てくれるので、f2の引数がnumber(少なくともnumberを含む型)だと推論してf()の呼び出しを見つけてエラーにしてくれる。

```flow
function f(a: string) {
  console.log(a)
}

function f2(a) {
  f(a)
}

f2(10); // エラーになる。
```

### dialyzerとの比較

dialyzerもエラーにしてくれる。Success Typingに従っても明らかなエラーであるため。

```elixir
defmodule Example do
  @spec f1(String.t) :: :ok
  defp f1(a) do
    IO.puts(a)
  end

  defp f2(a) do
    f1(a)
  end

  def main() do
    f2(10) # エラー。
    # f2('text') # OK
  end
end
```

## Any, None

`Any`は全てにマッチするし、`None`はないものにマッチする。

```python
from typing import Any

def f(a: Any) -> None:
    print(a)

f(10) # OK
f('text') # OK

from typing import Any

x: Any = 'text'
x = 10 # OK。その変数の含む値の型が変わる場合も許される。

z: bool = True
z = x # OK。引数の場合と同じで、Anyが持つ値を他の型にも入れることができてしまう。
```

この`Any`の挙動はflowの`any`も同じ。flowには任意の値を入れることはできるがそれが持つ値を更に利用させないための型として[mixed](https://flow.org/en/docs/types/mixed/)がある。

## NoReturn

```python
```

flowには`NoReturn`に相当するものがない。dialyzerでは`no_return`がこれに当たる。
