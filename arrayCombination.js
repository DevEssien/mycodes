const mainArr = ['a','b','c','d','e','f','g','h'];
const listComb = [];

function range(start, end) {
    const rangeList = [];
    for (let i = start; i <= end; i++) {
        rangeList.push(i);
    };
    return rangeList
};

function randrange(min, max) {
    let diff = Math.abs(max - min);
    let randint = Math.floor(Math.random() * diff) + min;
    return randint;
};

function arrayShuf(arraY) {
    const arr = arraY;
    let arrCopy = arr.slice();
    for (let j of range(0, arrCopy.length - 1)) {
        //let's shuffle the array by direct swapping
        rand = randrange(j, arrCopy.length);
        [arrCopy[j], arrCopy[rand]] = [arrCopy[rand], arrCopy[j]];
    };
    return arrCopy;
};

function arrayShuf(arraY) {
    const arr = arraY;
    let arrCopy = arr.slice();
    for (let j of range(0, arrCopy.length - 1)) {
        //let's shuffle the array by direct swapping
        rand = randrange(j, arrCopy.length);
        [arrCopy[j], arrCopy[rand]] = [arrCopy[rand], arrCopy[j]];
    };
    return arrCopy;
};

//factorial
function factorial(arr) {
    let loops = 1;
    for (let i = 2; i <= arr.length; i++) {
        loops *= i;
    };
    return loops;
};


let copyArr;
while (listComb.length !== factorial(mainArr)) {
    copyArr = arrayShuf(mainArr).slice();
    if (!(listComb.includes(copyArr))) {
        listComb.push(copyArr);
    };
}

console.log('array combination of', mainArr, 'is');
console.log(listComb);