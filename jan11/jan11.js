function reverseWords(s) {
    return s.split(' ').reverse().join(' ');
}

const input = "hello world";
const result = reverseWords(input);
console.log(result);