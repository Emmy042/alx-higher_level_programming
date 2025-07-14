#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Request error:', error.message);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Status code', response.statusCode);
    return;
  }

  try {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach(task => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 1;
        } else {
          completedTasks[task.userId]++;
        }
      }
    });

    console.log(completedTasks);
  } catch (err) {
    console.error('JSON parsing error:', err.message);
  }
});
