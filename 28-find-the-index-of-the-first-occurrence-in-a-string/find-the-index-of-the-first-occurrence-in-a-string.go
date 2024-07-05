import "strings"

func strStr(haystack string, needle string) int {
    for i := range haystack {
        if strings.HasPrefix(haystack[i:], needle) {
            return i
        }
    }
    return -1
}