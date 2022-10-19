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
    return `gcd is ${gcD}`;
}

console.log(gcd(34,4));


