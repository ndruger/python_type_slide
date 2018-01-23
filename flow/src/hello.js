// @flow

function f(a: {name: string, age: number}) {
  console.log(a)
}

// f({name: 10, age: 10}) // エラー。10がstrではない。
f({name: 'Bob', age: 10}) // OK
