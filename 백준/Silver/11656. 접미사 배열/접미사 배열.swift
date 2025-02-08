import Foundation 

var input = Array(readLine()!).map{String($0)}
var answer: [String] = []
var str: String = ""
while !input.isEmpty {
    str = input.removeLast() + str
    answer.append(str)
}
answer.sorted().forEach {
    print($0)
}