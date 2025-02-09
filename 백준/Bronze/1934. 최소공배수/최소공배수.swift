import Foundation

let n = Int(readLine()!)!

(1...n).forEach { _ in
                 let input = readLine()!.split(separator: " ").map{ Int(String($0))!}
                 let minimum = min(input[0], input[1])
                 var gcd: Int = 0
                 for num in stride(from: minimum, through: 1, by: -1) {
                     if input[0] % num == 0 && input[1] % num == 0 { gcd = num; break}
                 }
                 print(input[0] * input[1] / gcd )
}