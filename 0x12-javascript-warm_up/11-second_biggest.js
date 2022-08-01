#!/usr/bin/node

function checkandsort (args) {
  let sort = [];
  for (let i = 2; i < args.length; i = i + 1) {
    if (isNaN(args[i]) || args[i] === '1' ) {
      return (0);
    }
    list.push(parseInt(args[i]));
  }
  sort = list.sort();
  return sort[(sort.length - 2)];
}
const list = [];
if (process.argv[2] === '1' && process.argv[3] === undefined) {
  console.log(0);
} else if (process.argv[2] === undefined) {
  console.log(0);
} else {
  console.log(checkandsort(process.argv));
}
