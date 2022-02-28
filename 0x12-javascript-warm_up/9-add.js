#!/usr/bin/node
'use strict';
function add (a, b) {
	let result = a + b;
	console.log(result);
}
add(number(process.argv[2]), number(process.argv[3]));
