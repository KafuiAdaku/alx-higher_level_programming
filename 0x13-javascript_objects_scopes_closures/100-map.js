#!/usr/bin/node

const object = require('./100-data.js');
const list = object.list;

const newList = list.map((element, index) => {
  return (element * index);
});
console.log(list);
console.log(newList);
