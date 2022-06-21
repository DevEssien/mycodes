//range of start and end
function range(start, end) {
    const rangeList = [];
    for (let i = start; i <= end; i++) {
        rangeList.push(i);
    }
    return rangeList;
}
//console.log(range(1,5))

//range of random numbers from start to end exclusive
function randrange(min, max) {
    let diff = Math.abs(max - min);
    let randint = Math.floor(Math.random() * diff) + min;
    return randint;
}
//console.log(randrange(1,5));

//array shuffle
function arrayShuf(arraY) {
    const arr = arraY;
    let arrCopy = arr.slice();
    for (let j of range(0, arrCopy.length - 1)) {
        //let's shuffle the array by direct swapping
        rand = randrange(j, arrCopy.length);
        [arrCopy[j], arrCopy[rand]] = [arrCopy[rand], arrCopy[j]];
    }
    return arrCopy;
}
console.log(arrayShuf(['a','b','c','d','e','f','g','h','i','j']));