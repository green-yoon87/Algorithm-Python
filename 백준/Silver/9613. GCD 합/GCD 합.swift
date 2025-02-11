import Foundation 

let n = Int(readLine()!)!
var answer = 0 
(1...n).forEach {
    _ in
    answer = 0 
    let arr = readLine()!.split(separator: " ").map{ Int(String($0))!}
    for i in 1 ..< (arr.count - 1) {
        for j in (i + 1) ..< arr.count {
            answer += gcd(arr[j], arr[i])
        }
    }
    print(answer)
}

func gcd(_ num1: Int, _ num2: Int) -> Int {
    if num2 == 0 {
        return num1
    }
    return gcd(num2, num1 % num2)
}