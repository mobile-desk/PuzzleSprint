function decimalToBinary(decimalNumber) {
    return decimalNumber.toString(2);
}

function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Enter a decimal number: ', (input) => {
        const decimalNumber = parseInt(input);
        if (isNaN(decimalNumber) || decimalNumber < 0) {
            console.log("Please enter a valid non-negative integer.");
        } else {
            const binaryRepresentation = decimalToBinary(decimalNumber);
            console.log(`The binary representation of ${decimalNumber} is: ${binaryRepresentation}`);
        }
        rl.close();
    });
}

main();