import Foundation 

let n = Int(readLine()!)!
var arr: [Bool] = Array(repeating: true, count: 1000000 + 1)
arr[1] = false 
arr[0] = false
for i in 2...1000000  {
    if arr[i] {
        var n = 2
        while i * n <= 1000000 {
            arr[i * n] = false
            n += 1
        }
    }
}
(1...n).forEach {
    _ in
    let input = Int(readLine()!)!
    var answer = 0
    for i in stride(from: 3, through: input / 2, by: 2) {
       if arr[i] && arr[input - i]  { answer += 1 }
    }
    if arr[2] && arr[input - 2] { answer += 1}
    print(answer)
}