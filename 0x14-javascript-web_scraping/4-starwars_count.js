#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL as the first argument.');
  process.exit(1);
}

// Character URL to look for
const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Request error:', error.message);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  try {
    const data = JSON.parse(body);
    const films = data.results;

    // Count how many films include Wedge Antilles (character URL ID 18)
    const count = films.filter(film => film.characters.includes(wedgeUrl)).length;

    console.log(count);
  } catch (err) {
    console.error('Error parsing JSON:', err.message);
  }
});
