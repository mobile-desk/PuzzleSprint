const readline = require('readline');

function guessTheNumber() {
    const lowerBound = 1;
    const upperBound = 100;
    const targetNumber = Math.floor(Math.random() * (upperBound - lowerBound + 1)) + lowerBound;

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("Welcome to Guess the Number!");
    console.log(`Guess the number between ${lowerBound} and ${upperBound}`);

    let attempts = 0;

    rl.on('line', (userInput) => {
        const userGuess = parseInt(userInput);
        attempts++;

        if (userGuess === targetNumber) {
            console.log(`Congratulations! You guessed the correct number in ${attempts} attempts.`);
            rl.close();
        } else if (userGuess < targetNumber) {
            console.log("Too low! Try again.");
        } else {
            console.log("Too high! Try again.");
        }
    });
}

guessTheNumber();