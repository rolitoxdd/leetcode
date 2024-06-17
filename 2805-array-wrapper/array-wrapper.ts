class ArrayWrapper {
    public arr: number[];
    
    constructor(nums: number[]) {
        this.arr = nums;
    }
    
    valueOf(): number {
        let sum = 0;
        for (const n of this.arr) {
            sum += n;
        }
        return sum;
    }
    
    toString(): string {
        return `[${this.arr.join(',')}]`
    }
};

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */