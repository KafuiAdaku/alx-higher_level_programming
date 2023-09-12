#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || h <= 0) || (w === undefined || h === undefined)) {
      return ('Rectangle {}');
    }
    this.width = w;
    this.height = h;
  }

  print () {
  let square = '';
  for (let height = 0; height < this.height; height++) {
    for (let width = 0; width < this.width; width++) {
      square += 'X';
    }
    if (height !== this.height - 1) {
      square += '\n';
    }
  }
    if (square) {
      console.log(square);
    }
  }
};
