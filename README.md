# Python Type Hints

## 例

関数の引数と戻り値の型を指定

```python
def hello(a: str) -> bool:
    print("Hello " + a)
    return True

# hello(10) # エラー
hello("Python") # OK
```

### flowの構文の比較

```flow
function hello(a: string) {
  console.log("Hello " + a)
}

// hello(10); // エラー
hello("JavaScript");

```

## 変数の定義時に型を指定する

```python
# Python 3.5以前
# コメントで型指定。この場合型と値("text")が合わないのでエラー。
# s = "text" # type: int

s = 10 # type: int # OK

# Python 3.6ならコメントではなくまともな記法で変数に対しても型指定できる
s2: int = 10
```
