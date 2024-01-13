function countLegs(chickens, cows, pigs) {
    const chickenLegs = chickens * 2;
    const cowLegs = cows * 4;
    const pigLegs = pigs * 4;

    return chickenLegs + cowLegs + pigLegs;
}

// Example usage
const totalLegs = countLegs(2, 3, 5);
console.log("Total number of legs:", totalLegs);