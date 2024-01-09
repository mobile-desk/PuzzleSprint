function generateMultiplicationTable(number, rangeLimit) {
    console.log(`Multiplication table for ${number} up to ${number} * ${rangeLimit}:\n`);
    for (let i = 1; i <= rangeLimit; i++) {
        console.log(`${number} * ${i} = ${number * i}`);
    }
}

function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Enter a number: ', (number) => {
        rl.question('Enter the range: ', (rangeLimit) => {
            generateMultiplicationTable(parseInt(number), parseInt(rangeLimit));
            rl.close();
        });
    });
}

main();