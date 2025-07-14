#!/usr/bin/node

const fs = require('fs');

const filename = process.argv[2];
const text = process.argv[3]

if(!filename) {
    console.error('please provide a file name.');
    process.exit(1);
}

if(!text) {
    console.error('please provide a text content.');
    process.exit(1);
}

fs.writeFile(filename, text, 'utf8', (err, data)=> {
    if (err) {
        console.error('error writing file:', err.message);
        return;
    }
}
);

