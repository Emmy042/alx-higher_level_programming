#!/usr/bin/node

const http = require('http');
const https = require('https');

const url = process.argv[2];
const filename = process.argv[3];

if (!url || !filename) {
  console.error('Usage: ./script.js <url> <filename>');
  process.exit(1);
}

// Choose the correct module based on the URL protocol
const client = url.startsWith('https') ? https : http;

client.get(url, (res) => {
  let data = '';

  res.on('data', chunk => data += chunk);

  res.on('end', () => {
    require('fs').writeFile(filename, data, 'utf8', (err) => {
      if (err) return console.error('Write error:', err.message);
      console.log(`Saved content to ${filename}`);
    });
  });

}).on('error', (err) => {
  console.error('Request error:', err.message);
});
