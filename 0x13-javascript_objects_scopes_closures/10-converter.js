#!/usr/bin/node

exports.converter = function (base) {
  function Converttt (n) {
    return n.toString(base);
  }
  return Converttt;
};
