#!/usr/bin/node
// a script that reads and prints the content of a file
const fs = require('fs');

fs.readFile(process.argv[2], (err, contents) => {
  err ? console.log(err) : console.log(contents.toString());
});
