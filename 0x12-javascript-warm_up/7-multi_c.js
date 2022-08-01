#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i = i + 1) {
    console.log('C is fun');
  }
}
