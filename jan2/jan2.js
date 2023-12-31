function isPalindrome(str) {
    const formattedStr = str.toLowerCase().replace(/[^a-zA-Z0-9]/g, '');
    const reversedStr = formattedStr.split('').reverse().join('');
    return formattedStr === reversedStr;
}

const input = "A man, a plan, a canal, Panama";
const result = isPalindrome(input);
console.log(result);
