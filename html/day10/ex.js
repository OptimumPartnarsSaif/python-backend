    class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    // Method to display details
    displayDetails() {
        console.log(`Name: ${this.name}, Age: ${this.age}`);
    }
    }

    // Create objects
    const person1 = new Person("Alice", 25);
    const person2 = new Person("Bob", 30);

    // Use method
    person1.displayDetails();
    person2.displayDetails();
