#!/usr/bin/node

const arg = process.argv[2];

const int = Number(arg);

if (isNaN(int)) {
  console.log('missing number of occurrences');
} else {
  for (let i = 0; i < int; i++) {
    console.log('C is fun');
  }
}