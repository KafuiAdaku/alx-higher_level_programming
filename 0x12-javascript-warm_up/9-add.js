#!/usr/bin/node

function add (a, b) {
  return (a + b);
}
const int1 = Number(process.argv[2]);
const int2 = Number(process.argv[3]);
console.log(add(int1, int2));
