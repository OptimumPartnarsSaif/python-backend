    // Define a Car class
    class Car {
    constructor(brand, model, year, color) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.color = color;
        this.speed = 0; // default speed
    }

    // Method to start the car
    start() {
        console.log(`${this.brand} ${this.model} started.`);
    }

    // Method to accelerate
    accelerate(amount) {
        this.speed += amount;
        console.log(`${this.brand} ${this.model} is now going ${this.speed} km/h.`);
    }

    // Method to brake
    brake(amount) {
        this.speed -= amount;
        if (this.speed < 0) this.speed = 0;
        console.log(`${this.brand} ${this.model} slowed down to ${this.speed} km/h.`);
    }

    // Method to display info
    displayInfo() {
        console.log(
        `Car: ${this.brand} ${this.model} (${this.year}), Color: ${this.color}, Speed: ${this.speed} km/h`
        );
    }
    }

    // Create objects from the Car class
    const car1 = new Car("Toyota", "Corolla", 2020, "Blue");
    const car2 = new Car("Tesla", "Model 3", 2023, "White");

    // Use the methods
    car1.start();
    car1.accelerate(50);
    car1.brake(20);
    car1.displayInfo();

    car2.start();
    car2.accelerate(80);
    car2.displayInfo();
