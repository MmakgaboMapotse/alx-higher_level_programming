#!/usr/bin/node

const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint(c = 'X') {
    if (!this.width || !this.height) return;

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;

