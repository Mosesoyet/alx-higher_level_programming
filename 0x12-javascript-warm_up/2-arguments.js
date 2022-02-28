#!/usr/bin/node
'use strict';
let i = process.argv.length;
if (i === 2) {
	console.log('No argument');
} else if (i === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
