#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i = i + 1) {
    for (let a = 0; a < parseInt(process.argv[2]); a = a + 1) {
      process.stdout.write('#');
    }
    console.log();
  }
}
