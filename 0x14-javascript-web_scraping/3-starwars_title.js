#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch. Status code: ${response.statusCode}`);
    return;
  }

  try {
    const data = JSON.parse(body);
    console.log(data.title); // ✅ Print the movie title
  } catch (e) {
    console.error('Error parsing JSON:', e.message);
  }
});
