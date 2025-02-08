import Foundation

while let line = readLine()  {
    var input = Array(line).map{ String($0)}
    var answer: [Int] = [0, 0, 0, 0]
    if input.isEmpty { break }
    for str in input {
        if Character(str).isLowercase {
            answer[0] += 1
        } else if  Character(str).isUppercase {
            answer[1] += 1
        } else if let _ = Int(str) {
            answer[2] += 1
        } else if str == " " {
            answer[3] += 1
        } 
    }
    print(answer.map{String($0)}.joined(separator: " "))
}