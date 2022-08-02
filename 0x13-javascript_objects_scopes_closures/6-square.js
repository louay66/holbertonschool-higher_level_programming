#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.width; i++) {
          process.stdout.write('X');
        }
        console.log();
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.width; i++) {
          process.stdout.write('C');
        }
        console.log();
      }
    }
  }
}
module.exports = Square;
