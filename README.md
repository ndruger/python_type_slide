# Python Type Hints

Python Type Hintsのmypyの動作を他の後付け静的型チェックと比較して見ていく。


## 例

関数の引数と戻り値の型を指定

```python
def f(a: str) -> bool:
    print('Hello ' + a)
    return True

# f(10) # NG。10がstrではない。
f('Python') # OK
```

### flowの構文との比較

```javascript
function f(a: string): boolean {
  console.log('Hello ' + a);
  return true;
}

// f(10); // NG。10がstringではない。
f('JavaScript');

```


## 変数の定義時に型を指定する

```python
# Python 3.5以前は、コメントで型指定。
s = 10 # type: int
# s = 'text' # type: int # NG。この場合型と値('text')が合わない。


# Python 3.6ならコメントではない記法で型指定できる
s2: int = 10
```


## List

```python
from typing import List

def f1(a: List[float]):
    print(a)

#f1(['a']) # NG。要素がfloatではない。
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

#f(('a', 'b', 'c')) # NG。3番目ばintではない。
f(('a', 'b', 1)) # OK
```


## Dict

```python
from typing import Dict

def f(a: Dict[str, str]):
    print(a)

#f({'name': 10}) # NG。10がstrではない。
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

// f({name: 10, age: 10}) // NG。10がstringではない。
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

```javascript
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
    f2(10) # NG。
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


## キャスト

型の上ではエラーとなるが実際には問題ないケース。つまり、型は`List[object`だが処理としては確実にその要素は文字列を持っている場合など、キャストしないと型チェックを通らないので、キャストを利用する。

```python
from typing import cast

def f(a: str):
    print(a)

# f(10) # NG。10がstrではない。
f(cast(str, 10)) # OK。エラーにはならない。ただ、この使い方はおかしい。
```


## Union type

`Unicon["a", "b"]`などはできない。そのような場合enumを使って実現する((Support for singleton types in unions)[https://www.python.org/dev/peps/pep-0484/#support-for-singleton-types-in-unions])。

```python
from typing import Union, List

def f1(a: Union[int, str]):
    print(a)

def f2(a: List[Union[int, str]]):
    print(a)


# f1(0.5) # NG。0.5はintでもstrでもない。
f1("text") # OK

# f2(["text", 10, 0.5]) # NG。0.5はintでもstrでもない。
f2(["text", 10]) # OK
```

### flowとの比較

flowはリテラルを型と同じようにUnionできる。

```javascript
type Dir = 'up' | 'down' | number

function f(a: Dir) {
  console.log(a);
}

// f('right'); // NG。'right'は'up'でも'down'でもintでもない。
f('up'); // OK
f(5); // OK
```


## Optional

`Optional[X]`は`Union[X, type(None)]`と同じ。


## クラス

クラスの型チェックはNominal Typingで行われる。Structural Typingではない。
サブクラスは許可される。

```python
class MySuperClass:
    super_name: str

class MyClass1(MySuperClass):
    name: str

class MyClass2(MySuperClass):
    name: str

class MySubClass(MyClass1):
    sub_name: str

def f(a: MyClass1):
    print(a)

f(MyClass1()) # OK
# f(MyClass2()) # NG。Nominal Typingなので同じ構造でもエラーになる。
# f(MySuperClass()) # NG。superはNG。
f(MySubClass()) # OK。サブクラスはOK。

o = MyClass1()
# o.name = 2 # NG。2はstrではない。
# o.method_a() # NG。method_aというメソッドを持たない。
```

### flowとの比較

flowのクラスもNominal Typingでチェックされる。

```javascript
class A {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}
// Aと同じ構造
class B {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}

function f(a: A) {
  return 'Hello, ' + a.name;
}

f(new A('bob'));  // OK
f(new B('bob'));  // NG。Nominal Typingなのでクラスが異なるとエラー。
```

共通に許可したい場合インターフェースを定義する。(Classes are nominally typed )[https://flow.org/en/docs/lang/nominal-structural/#toc-classes-are-nominally-typed]

### typescriptとの比較

typescriptのクラスはStructural Typingでチェックされるので外部IFが同じならエラーにならない。

```typescript
class A {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}
// Aと同じ構造
class B {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}
// Aと異なる構造
class C {
  fullName: string;
  constructor(fullName: string) {
    this.fullName = fullName;
  }
}

function f(a: A) {
  return 'Hello, ' + a.name;
}

f(new A('bob'));  // OK
f(new B('bob'));  // OK。Structural Typingなのでクラスが異なっていてもいい。
f(new C('bob'));  // NG。外部IFが異なるのでエラー。
```

## NewType

NewTypeを使って新規にNominal Typingで扱われる型を作ることができる。

```python
from typing import NewType, cast, Any

TypeX = NewType('TypeX', int)

def f(a: TypeX):
    print(a + 1)

# f(10) # NG。intはTypeXではない。Nominal Typingなのでエラーになる。
f(TypeX(10)) # OK
#f(TypeX(1) + TypeX(2)) # NG。足すとintになるのでTypeXではない
```


## Generics

定義可能。詳細は省略。


## おまけ: flowがどの程度型の操作ができるのか？

型を操作して組み合わせて別の型を作れる。

```javascript
type A = {name: string, age: number, height: number};
type B = {age: number};
type C = $Diff<A, B>; // 結果は{name: string, height: number}。

function f1(a: C) {
  console.log(a);
}

f1({name: 'bob', height: 10}) // OK

type FieldName = $ElementType<C, 'name'> // 結果はstring

function f2(a: FieldName) {
  console.log(a);
}

// f2(10) // NG。10はstringではない
f2('bob')

type D = {name: FieldName, weight: number} // 結果は{name: string, weight: number}。

function f3(a: D) {
  console.log(a);
}

// f3({name: 1, weight: 10}) // NG。1はstringではない。
f3({name: 'bob', weight: 10}) // OK
```
