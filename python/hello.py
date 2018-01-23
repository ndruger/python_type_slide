
# 関数の引数と戻り値の型を指定
def hello(lang: str) -> bool:
    print("Hello " + lang)
    return True

# hello(10) # エラー
hello("Python") # OK


# 変数の定義時にコメントで型指定。この場合型と値("text")が合わないのでエラー。
# s = "text" # type: int

s = 10 # type: int # 成功するケース


# Python3.6ならコメントではなくまともな記法で変数に対しても型指定できる
s2: int = 10
