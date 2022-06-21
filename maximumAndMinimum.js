

const list = [2,6,4,32,5,1,6,47,56,84,7,458,47,6,457,4572,4572,7,236,7,3,7,34];

function maxAndMin(arr) {
    let max = arr[0];
    let min = arr[0];

    for (elem of arr) {
        if (elem < min) min = elem;
        if (elem > max) max = elem;
    }
    return `maximum number in the array is ${max} and the minimum number is ${min}`
}

console.log(maxAndMin(list));