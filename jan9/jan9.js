function permute(nums) {
    const result = [];

    function backtrack(current, remaining) {
        if (remaining.length === 0) {
            result.push([...current]);
        } else {
            for (let i = 0; i < remaining.length; i++) {
                current.push(remaining[i]);
                backtrack(current, remaining.slice(0, i).concat(remaining.slice(i + 1)));
                current.pop();
            }
        }
    }

    backtrack([], nums);
    return result;
}

const input = [1, 2, 3];
const result = permute(input);
console.log(result);