#!/usr/bin/node

const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let square = '';
      for (let height = 0; height < this.height; height++) {
        for (let width = 0; width < this.width; width++) {
          square += c;
        }
        if (height !== this.height - 1) {
          square += '\n';
        }
      }
      if (square) {
        console.log(square);
      }
    }
  }
};
