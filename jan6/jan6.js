function firstNonRepeatingChar(s) {
    const charMap = new Map();
    for (let char of s) {
        charMap.set(char, (charMap.get(char) || 0) + 1);
    }
    for (let char of s) {
        if (charMap.get(char) === 1) {
            return char;
        }
    }
    return ' ';
}

const input = "leetcode";
const result = firstNonRepeatingChar(input);
console.log(result);