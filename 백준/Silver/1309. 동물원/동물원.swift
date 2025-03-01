import Foundation 

let n = Int(readLine()!)!
var dp: [[Int]] = Array(repeating: Array(repeating: 0, count:3), count: 100000 + 1)
dp[1] = [1, 1, 1]
if n > 1 {
    (2...n).forEach {
        let previousLine = dp[$0 - 1]
        let nothing = previousLine.reduce(0, +) % 9901
        let leftLion = (previousLine[0] + previousLine[2]) % 9901
        let rightLion = (previousLine[0] + previousLine[1]) % 9901
        dp[$0] = [nothing, leftLion, rightLion]
    }
}
print(dp[n].reduce(0, +) % 9901)