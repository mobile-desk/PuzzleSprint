function manualSort(inputArray) {
    const n = inputArray.length;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (inputArray[j] > inputArray[j + 1]) {
                // Swap elements if they are in the wrong order
                [inputArray[j], inputArray[j + 1]] = [inputArray[j + 1], inputArray[j]];
            }
        }
    }
}

function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Enter a list of space-separated numbers: ', (input) => {
        const inputArray = input.split(' ').map(Number);

        console.log('Original List:', inputArray);

        manualSort(inputArray);

        console.log('Sorted List:', inputArray);

        rl.close();
    });
}

main();