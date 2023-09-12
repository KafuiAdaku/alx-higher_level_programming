#!/usr/bin/node

const array = process.argv;
let max = 0;
let max2nd = 0;
const arrayLength = array.length;

if (arrayLength - 2 === 0) {
  console.log(0);
} else if (arrayLength - 2 === 1) {
  console.log(0);
} else {
  for (let index = 2; index < arrayLength; index++) {
    if (Number(array[index]) > max) {
      max2nd = max;
      max = array[index];
    }
  }
  console.log(max2nd);
}
