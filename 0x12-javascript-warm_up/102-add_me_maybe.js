#!/usr/bin/node
// A function that  executes x times a function.

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
