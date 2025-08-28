const name = "Sara";
const age = 25;
console.log(`Hello, my name is ${name} and I am ${age} years old.`);
// Array destructuring
const numbers = [10, 20, 30];
const [first, second, third] = numbers;
console.log(first, second, third); // 10 20 30

// Object destructuring
const person = { name: "Ali", city: "Amman", country: "Jordan" };
const { name: personName, city } = person;
console.log(personName, city); // Ali Amman
