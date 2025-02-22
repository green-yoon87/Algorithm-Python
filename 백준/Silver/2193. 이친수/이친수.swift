import Foundation 

let n = Int(readLine()!)!
var dp: [[Int]] = Array(repeating: Array(repeating:0, count:2), count: 90 + 1)

dp[1] = [1, 1]

if n > 1 {
    for row in 2...n {
        dp[row][0] = dp[row - 1][0] + dp[row - 1][1]
        dp[row][1] = dp[row - 1][0]
    }
}
print(dp[n][1])