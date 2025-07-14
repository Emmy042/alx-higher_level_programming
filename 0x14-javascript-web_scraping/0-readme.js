#!/usr/bin/node

const fs = require('fs');

const filename = process.argv[2];

if(!filename) {
    console.error('please provide a file name.');
    process.exit(1);
}

fs.readFile(filename, 'utf8', (err, data)=> {
    if (err) {
        console.error('error reading file:', err.message);
        return;
    }
    console.log(data);
}
);

