// Create an array
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Use map to double each number
let doubled = numbers.map(num => num * 2);

// Use map to turn numbers into strings
let asStrings = numbers.map(num => `Number: ${num}`);

// Use filter to get only even numbers
let evens = numbers.filter(num => num % 2 === 0);

// Use filter to get numbers greater than 5
let greaterThanFive = numbers.filter(num => num > 5);

console.log("Original:", numbers);
console.log("Doubled:", doubled);
console.log("As Strings:", asStrings);
console.log("Evens:", evens);
console.log("Greater than 5:", greaterThanFive);
