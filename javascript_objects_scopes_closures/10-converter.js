#!/usr/bin/node
// a function that converts a number from base 10 to another base passed as argument
exports.converter = function (base) {
  return (number = 0) => number.toString(base);
};
