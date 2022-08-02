#!/usr/bin/node

exports.esrever = function (list) {
  const revers = [];
  for (let i = 0; i < list.length; i++) {
    revers.unshift(list[i]);
  }
  return revers;
};
