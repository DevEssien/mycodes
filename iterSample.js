
const arr = [1,2,3,4,5,6,7,8,9,10,11];

function sample(iter, len) {
    const sampled = [];
    let rand;
    let popped;

    if (len <= iter.length) {
        for (let i = 0; i < len; i++) {
            rand = Math.floor(Math.random() * (iter.length -1)); //iter.length sets the range to the length of the array
            popped = iter.splice(rand, 1); //popped = [element] // e.g : popped = [9]
            sampled.push(popped[0]); //push(element at index 0 of popped) for instance : popped[0] = 9
        }
        return sampled;
    }
    return `length provided must be less than or equal to the length of the array \nlength of the array is ${iter.length}`
}

console.log(sample(arr, 10));
