// @flow

function f(a: string) {
  console.log(a)
}

function f2(a) {
  f(a)
}

f2(10); // エラーになる。
