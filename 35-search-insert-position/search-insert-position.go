func searchInsert(nums []int, target int) int {
    low := 0
    high := len(nums)
    mid := (low + high) / 2
    
    for low < high {
        if nums[mid] == target {
            return mid
        } else if target < nums[mid] {
            high = mid
            mid = (low + high) / 2
        } else {
            low = mid + 1
            mid = (low + high) / 2
        }
    }
    return mid
}