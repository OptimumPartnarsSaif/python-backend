function greetUser(name = "Guest", ...hobbies) {
  console.log(`Welcome, ${name}!`);
  if (hobbies.length > 0) {
    console.log(`Your hobbies are: ${hobbies.join(", ")}`);
  } else {
    console.log("You didn't share any hobbies.");
  }
}

// Examples
greetUser("Omar", "Reading", "Football", "Coding");
greetUser();
