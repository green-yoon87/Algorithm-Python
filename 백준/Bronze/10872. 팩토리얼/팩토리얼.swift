import Foundation 

let n = Int(readLine()!)!
func factorial(_ num: Int) -> Int {
    if n == 0 { return 1}
    var answer = 1 
    for i in 1...n {
        answer *= i 
    }
    return answer 
}
print(factorial(n))