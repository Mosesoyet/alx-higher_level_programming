#!/usr/bin/node
function add (a, b) {
  let result = a + b;
  console.log(result);
}

add(Number(process.argv[2]), Number(process.argv[3]));
