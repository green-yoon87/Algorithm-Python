import Foundation

let nums = Array(readLine()!).map{ String($0)}
var answer = ""
for (idx, num) in nums.enumerated() {
    var str = String(Int(num, radix: 8)!, radix: 2)
    if idx != 0 {
        if str.count % 3 == 1 { str = "00" + str}
        else if str.count % 3 == 2 { str = "0" + str}
    } 
    answer += str
}
print(answer)