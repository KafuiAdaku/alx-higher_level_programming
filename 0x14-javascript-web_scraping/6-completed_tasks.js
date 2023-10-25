#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode !== 200) {
    console.error(response && response.statusCode);
  } else {
    const todos = JSON.parse(body);
    const completedTodos = [];

    for (const todo of todos) {
      if (todo.completed) {
        completedTodos.push(todo);
      }
    }

    const userTask = {};

    for (const todo of completedTodos) {
      if (!(todo.userId in userTask)) {
        userTask[todo.userId] = 1;
      } else {
        userTask[todo.userId]++;
      }
    }

    console.log(userTask);
  }
});
