func threeConsecutiveOdds(arr []int) bool {
    for i := 0 ; i < len(arr) - 2 ; i++ {
        n0 := arr[i]
        n1 := arr[i+1]
        n2 := arr[i+2]
        if n0 % 2 == 1 && n1 % 2 == 1 && n2 % 2 == 1 {
            return true
        }
    }
    return false
}