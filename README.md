# Python Type Hints

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
# Python 3.5以前
# コメントで型指定。

s = 10 # type: int
# s = 'text' # type: int # エラー。この場合型と値('text')が合わない。


# Python 3.6ならコメントではなくまともな記法で型指定できる
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

```
def f(a: Dict[str, str]):
    print(a)

#f({'name': 10}) # エラー。10がstrではない。
f({'name': 'value'}) # OK
```

Dictのフィールドごとの型指定はできない。[issue](https://github.com/python/typing/issues/28)で議論はされている。

[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)ならばフィールド毎の型指定が可能だが、DictとNamedTupleはそもそも使い方が大分違うので微妙。

### flowとの比較

flowはobjectに対するフィールドごとの型指定ができる。

```javascripot
function f(a: {name: string, age: number}) {
  console.log(a)
}

// f({name: 10, age: 10}) // エラー。10がstringではない。
f({name: 'Bob', age: 10}) // OK

```
