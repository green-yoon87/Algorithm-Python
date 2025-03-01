import Foundation 

let n = Int(readLine()!)!
var dp: [[Int]] = Array(repeating: Array(repeating: 0, count: 3), count: 1000 + 1)
(1...n).forEach {
    let inputArr = readLine()!.split(separator: " ").map{ Int(String($0))!}
    if $0 == 1 { dp[$0] = inputArr }
    else {
        let previousPrice = dp[$0 - 1]
        let red = min(previousPrice[1], previousPrice[2]) + inputArr[0]
        let green = min(previousPrice[0], previousPrice[2]) + inputArr[1]
        let blue = min(previousPrice[0], previousPrice[1]) + inputArr[2]
        dp[$0] = [red, green, blue]
    }
}
print(dp[n].min()!)