
const arr = [23,5,3,67,2,43,65,4,5,7,88,5,34,7,434,5,6,2,65,4,78,9,8,7,3,55,7,546,45,4,1,535,74,6,5,7999,53,3];

function bubbleSort(list) {
    for (let i = 0; i < list.length; i++) {
        for (let j = 0; j < list.length; j++) {
            if (list[j+1] < list[j]) {
                [list[j+1], list[j]] = [list[j], list[j+1]];
            };
        };
    };
    return list;
};
console.log(bubbleSort(arr));