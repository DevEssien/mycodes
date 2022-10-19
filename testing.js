
const nums = [2,7,11,15];
let target = 2;

for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i+1] + nums[i] === target) {
        console.log([i, i+1]);
    }
    if (nums[i] === target) {
        console.log(i);
    }
    if (nums[i+1] === target) {
        console.log(i+1);
    }else if () {
        console.log('not found');
    }
}