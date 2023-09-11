#!/usr/bin/node
/**
 * a script that prints a square
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 * You must use the character X to print the square
 * You must use console.log(...) to print all output
 * You are not allowed to use `var`
 * You must use a loop (while, for, etc.)
 */

if (Number(process.argv[2])) {
  const count = process.argv[2];
  let square = '';
  for (let outer = 0; outer < count; outer++) {
    for (let inner = 0; inner < count; inner++) {
      square += 'X';
    }
    if (outer !== count - 1) {
      square += '\n';
    }
  } if (square) {
    console.log(square);
  }
} else {
  console.log('Missing size');
}
