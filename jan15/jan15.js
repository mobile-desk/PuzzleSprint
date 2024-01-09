function calculateFactorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    } else {
        return n * calculateFactorial(n - 1);
    }
}

function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Enter a number to calculate its factorial: ', (number) => {
        const n = parseInt(number);
        if (isNaN(n) || n < 0) {
            console.log("Please enter a valid non-negative integer.");
        } else {
            const result = calculateFactorial(n);
            console.log(`The factorial of ${n} is: ${result}`);
        }
        rl.close();
    });
}

main();