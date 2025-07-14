#!/usr/bin/node

const https = require('https');

const server = process.argv[2];

if (!server) {
  console.error('Please enter a valid URL');
  process.exit(1);
}

https.get(server, (res) => {
  console.log('Status Code:', res.statusCode);

  let data = '';

  res.on('data', (chunk) => {
    data += chunk;
  });


}).on('error', (err) => {
  console.error('Request Error:', err.message);
});
