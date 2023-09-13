#!/usr/bin/node

const filePathA = process.argv[2].toString();
const filePathB = process.argv[3].toString();
const concatFile = process.argv[4].toString();

const fs = require('fs');

fs.readFile(filePathA, 'utf-8', (err, dataA) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  fs.readFile(filePathB, 'utf-8', (err, dataB) => {
    if (err) {
      console.error('Error:', err);
      return;
    }
    const concatData = dataA + dataB;
    fs.appendFile(concatFile, concatData, 'utf-8', (err) => {
      if (err) {
        console.error('Error:', err);
      }
    });
  });
});
