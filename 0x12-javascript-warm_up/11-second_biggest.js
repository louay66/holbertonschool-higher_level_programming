#!/usr/bin/node

function checkandsort (args) {
  let sort = [];
  for (let i = 2; i < args.length; i = i + 1) {
    if (isNaN(args[i])) {
      return (0);
    }
    list.push(parseInt(args[i]));
  }
  sort = list.sort();
  return sort[(sort.length - 2)];
}
const list = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(checkandsort(process.argv));
}
