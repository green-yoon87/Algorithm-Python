import Foundation 

let n = Int(readLine()!)!
var dp: [[Int]] = Array(repeating: Array(repeating:0 , count: 10), count: 1000 + 1)
dp[1] = Array(repeating: 1, count: 10)

if n > 1 {
    (2...n).forEach {
        var previousArr = dp[$0 - 1]
        var sum = 0 
        for i in stride(from: 9 , through: 0, by: -1) {
            sum += previousArr.removeLast()
            dp[$0][i] = sum  % 10007
        }
    }
}
print(dp[n].reduce(0, +) % 10007)