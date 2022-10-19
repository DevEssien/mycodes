
function gcd(numerator, denominator) {
    let divisor = numerator < denominator ? numerator : denominator;
    let dividend = numerator > denominator ? numerator : denominator;
    let rem = dividend % divisor;

    while (rem !== 0) {
        dividend = divisor;
        divisor = rem;
        rem = dividend % divisor;
    }

    let gcD = divisor;
    return gcD;
}

console.log(gcd(35,5));


function lcm(a,b){
    let lcM = (a*b) / gcd(a,b);
    return lcM;
}
console.log(lcm(4,12));



// function primePrinter(no) {
//     if (no >= 2) {
//         console.log(2);
//     }

//     if (no >= 3) {
//         console.log(3);
//     }

//     for (let i = 2; i <= no + 1; i++) {
//         if ((i % 3 !==0) && (i % 2 !== 0)) {
//             console.log(i);
//         }
//     }
// }

// primePrinter(200);

// function fibonacciSeries(len) {
//     let A = 0;
//     let B = 1;
//     let storedA;
//     while (len > 0) {
//         storedA = A;
//         A = B;
//         B = A + storedA;
//         console.log(storedA);
//         len -= 1
//     }
// }
// fibonacciSeries(20);

// function factorial(num) {
//     let n = 1;
//     for (let j = 2; j <= num; j++) {
//         n *= j;
//     }
//     return n;
// }

// function permutation(n, r) {
//     let result1 = factorial(n) / factorial(n - r);
//     return result1;
//     return `${n}P${r} = ${result1}`
// }
// console.log(permutation(5,5));

// function combination(n, r) {
//     let result2 = factorial(n) / (factorial(n - r) * factorial(r));
//     return result2;
//     return `${n}C${r} = ${result2}`
// }
// console.log(combination(5,5));