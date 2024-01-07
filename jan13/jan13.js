const readline = require('readline');

function calculateSum(numbers) {
    return numbers.reduce((acc, curr) => acc + curr, 0);
}

function main() {
    const numbers = [];
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("Enter numbers. Press 's' to calculate the sum.");

    rl.on('line', (input) => {
        if (input.toLowerCase() === 's') {
            if (numbers.length > 0) {
                const totalSum = calculateSum(numbers);
                console.log(`The sum of the entered numbers is: ${totalSum}`);
            } else {
                console.log("No numbers were entered.");
            }
            rl.close();
        } else {
            const number = parseFloat(input);
            if (!isNaN(number)) {
                numbers.push(number);
            } else {
                console.log("Invalid input. Please enter a valid number or 's' to calculate the sum.");
            }
        }
    });
}

main();