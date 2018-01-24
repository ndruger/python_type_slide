var A = /** @class */ (function () {
    function A(name) {
        this.name = name;
    }
    return A;
}());
// Aと同じ外部IF
var B = /** @class */ (function () {
    function B(name) {
        this.name = name;
    }
    return B;
}());
// Aと異なる外部IF
var C = /** @class */ (function () {
    function C(fullName) {
        this.fullName = fullName;
    }
    return C;
}());
function f(a) {
    return 'Hello, ' + a.name;
}
f(new A('bob'));
f(new B('bob'));
f(new C('bob'));
