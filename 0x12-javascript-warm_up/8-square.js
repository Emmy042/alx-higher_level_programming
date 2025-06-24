#!/usr/bin/node

const arg = process.argv[2];

const int = Number(arg);

if (isNaN(int)) {
  console.log('missing size');
} else {
  for (let i = 0; i < int; i++) {
    console.log('X'.repeat(int));
}
}