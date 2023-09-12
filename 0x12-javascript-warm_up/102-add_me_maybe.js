#!/usr/bin/node

exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  const newNumber = number + 1;
  theFunction(newNumber);
};
