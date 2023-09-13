#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  let revIdx = list.length - 1;
  let index = 0;

  for (index, revIdx; index < list.length; index++, revIdx--) {
    reversed[index] = list[revIdx];
  }
  return (reversed);
};
