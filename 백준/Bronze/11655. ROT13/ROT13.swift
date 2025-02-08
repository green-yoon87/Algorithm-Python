import Foundation 

let input = Array(readLine()!).map{ String($0)}
let lowerAlphabet = Array("abcdefghijklmnopqrstuvwxyz").map{ String($0)}
let upperAlphabet = lowerAlphabet.map{ Character($0).uppercased() }

var answer: String = ""
for str in input {
    if str == " " { answer += str }
    else if let _ = Int(str) {answer += str }
    else {
        if Character(str).isLowercase {
            if let index = lowerAlphabet.firstIndex(of: str) {
                answer += lowerAlphabet[getIndex(index)]
            }
        } else {
            if let index = upperAlphabet.firstIndex(of: str) {
                answer += upperAlphabet[getIndex(index)]
            }
        }
    }
}
print(answer)

func getIndex(_ index: Int) -> Int {
    if index + 13 > 25 { return index + 13 - 26}
    return index + 13
}