function parent() {
  console.log("ok");
  const a = 10;
  const b = 20;
  function child1() {
    let sum = a + b;
    return sum;
  }
  function child2(a, b) {
    let sum2 = a + b;
    return sum2;
  }
  return {
    child2: child2(a, b),
  };
}
var foo = parent();
foo.child2();

console.log(foo.child2());
