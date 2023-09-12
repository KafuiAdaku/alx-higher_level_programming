#!/usr/bin/node

function factorial (n) {
  if (n === 0) {
    return (1);
  }
  return n * (factorial(n - 1));
}

const integer = Number(process.argv[2]);
if (isNaN(integer)) {
  console.log(1);
} else {
  console.log(factorial(integer));
}
