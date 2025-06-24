6-multi_languages_loop.js

const num = process.argv[2];

const int = Number(num);

if (isNaN(int)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${int}`);
}