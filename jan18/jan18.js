const readline = require('readline');

function calculateCircleArea(radius) {
    return Math.PI * radius**2;
}

function calculateSquareArea(sideLength) {
    return sideLength**2;
}

function calculateTriangleArea(base, height) {
    return 0.5 * base * height;
}

function main() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("Choose a geometric shape:");
    console.log("1. Circle");
    console.log("2. Square");
    console.log("3. Triangle");

    rl.question("Enter the number corresponding to the shape: ", (choice) => {
        if (choice === '1') {
            rl.question("Enter the radius of the circle: ", (radius) => {
                const area = calculateCircleArea(parseFloat(radius));
                console.log(`The area of the circle is: ${area}`);
                rl.close();
            });
        } else if (choice === '2') {
            rl.question("Enter the side length of the square: ", (sideLength) => {
                const area = calculateSquareArea(parseFloat(sideLength));
                console.log(`The area of the square is: ${area}`);
                rl.close();
            });
        } else if (choice === '3') {
            rl.question("Enter the base length of the triangle: ", (base) => {
                rl.question("Enter the height of the triangle: ", (height) => {
                    const area = calculateTriangleArea(parseFloat(base), parseFloat(height));
                    console.log(`The area of the triangle is: ${area}`);
                    rl.close();
                });
            });
        } else {
            console.log("Invalid choice. Please choose a valid option.");
            rl.close();
        }
    });
}

main();