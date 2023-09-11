#!/usr/bin/node

if (Number(process.argv[2])) {
  const count = Number(process.argv[2]);
  for (let index = 0; index < count; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
