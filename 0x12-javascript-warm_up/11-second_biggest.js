#!/usr/bin/node

function checkandsort (args) {
  let sort = [];
  let bool = 1;

  for (let i = 2; i < args.length; i = i + 1) {
    if (isNaN(args[i])) {
      return (0);
    } else if (args[i] > 0) {
      bool += 1;
    }
    list.push(parseInt(args[i]));
  }

  sort = list.sort();
  if (bool === 1) {
    return sort[1];
  } else if (bool === 2) {
    return sort[0];
  } else {
    return sort[(sort.length - 2)];
  }
}
const list = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(checkandsort(process.argv));
}
