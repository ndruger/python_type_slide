
class A {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}
// Aと同じ外部IF
class B {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}
// Aと異なる外部IF
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
