// @flow

function f(a: string) {
  console.log(a)
}

function f2(a) {
  f(a);
}

let anyX: any = 'text';

let mixedX: mixed = 'text';

let z: string = 'a'
// z = anyX  // OK。anyはその中の値の型がなんであれ、別の型の変数に渡せる。
z = mixedX  // エラー。mixedの場合は任意の型を入れることができるが、それを別の型の変数に入れる時にミスマッチならばエラーになる。
