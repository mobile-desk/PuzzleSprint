//npm install say

const say = require('say');

function textToSpeech(text, language = 'en') {
    say.export(text, language, 1.0, 'output.wav', (err) => {
        if (err) {
            return console.error(err);
        }
        say.play('output.wav');
    });
}

function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Enter the text you want to convert to speech: ', (userInput) => {
        textToSpeech(userInput);
        rl.close();
    });
}

main();