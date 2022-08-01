#!/usr/bin/node

const add = (a, b) => { const c = a + b; return c; };
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
