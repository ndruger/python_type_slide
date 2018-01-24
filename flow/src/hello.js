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
// z = anyX  // OK。同じく入れることができる。
z = mixedX  // エラー。
