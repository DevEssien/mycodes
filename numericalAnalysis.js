//NUMERICAL ANALYSIS MEG303: USING BISECTION  METHOD

let analytical;
let num = 0;
let upperLim = 1.5;
let lowerLim = 0;
let mean;
let functionMid;
let relativeErr;
let error;
let negativeNum;

const func = (no) => {
    const f = no ** 8 - 1;
    return f;
};

const midLim = (upperLim, lowerLim) => {
    const result = (upperLim + lowerLim) / 2;
    return result;
};

while (num >= 0) {
    negativeNum = num * -1;
    if (func(num) === 0) {
        analytical = num;
        break;
    } else if (func(negativeNum) === 0) {
        analytical = negativeNum;
        break;
    }

    num += 1;
}

const relativeError = (trueVal, approx) => {
    const relError = (100 * (trueVal - approx)) / trueVal;
    return Math.abs(relError);
};
let n = 0;
while (lowerLim <= analytical - 0.01) {
    mean = midLim(upperLim, lowerLim);
    functionMid = func(mean);
    if (functionMid >= 0) {
        upperLim = mean;
    } else {
        lowerLim = mean;
    }
    relativeErr = relativeError(analytical, mean);
    // // console.log("mean = ", mean);
    // // console.log("function of mid = ", functionMid);
    // console.log("relative error = ", relativeErr);
    n++;
}
console.log("no of iterations = ", n);
console.log("analytical value = ", analytical);
console.log("relative error = ", relativeErr);
