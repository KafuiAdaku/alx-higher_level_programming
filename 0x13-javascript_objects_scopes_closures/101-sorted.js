#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

for (const userId in dict) {
  const occurance = dict[userId];
  if (!newDict[occurance]) {
    newDict[occurance] = [];
  }
  newDict[occurance].push(userId);
}
console.log(newDict);
