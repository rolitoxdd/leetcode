function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const returnedArray: number[] = [];
    for (const index in arr) {
        const value: number = arr[index];
        const newValue: number = fn(value, +index);
        returnedArray.push(newValue);
    }
    return returnedArray;
};