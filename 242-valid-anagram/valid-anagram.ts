function isAnagram(s: string, t: string): boolean {
    if (s.length != t.length) {
        return false;
    }
    const letterCount = {}
    for (const c of s) {
        if (letterCount[c]) {
            letterCount[c]++;
        } else {
            letterCount[c] = 1
        }
    }

    for (const c of t) {
        if (!(c in letterCount)) {
            return false;
        }
        letterCount[c]--;
        if (letterCount[c] < 0) {
            return false;
        }
    }
    return true;

};