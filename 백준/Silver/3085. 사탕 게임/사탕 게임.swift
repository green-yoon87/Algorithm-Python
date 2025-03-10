import Foundation

let n = Int(readLine()!)!
var candyBasket: [[String]] = []
(1...n).forEach { _ in
    candyBasket.append(Array(readLine()!).map{ String($0)})
}

func swap(_ p1: (Int, Int), _ p2: (Int, Int)) {
    let temp = candyBasket[p1.0][p1.1]
    candyBasket[p1.0][p1.1] = candyBasket[p2.0][p2.1]
    candyBasket[p2.0][p2.1] = temp
}

func checkMaxLength(_ candyBasket: [[String]]) -> Int {
    var maxLength: Int = 1
    for i in 0...(candyBasket.count - 1) {
        var beforeRow = candyBasket[i][0]
        var beforeColumn = candyBasket[0][i]
        var rowLength = 1
        var columnLength = 1
        for j in 1...(candyBasket.count - 1) {
            if candyBasket[i][j] == beforeRow { rowLength += 1}
            else {rowLength = 1; beforeRow = candyBasket[i][j]}
            
            if candyBasket[j][i] == beforeColumn { columnLength += 1 }
            else {columnLength = 1; beforeColumn = candyBasket[j][i] }
            maxLength = max(rowLength, max(columnLength, maxLength))
            if maxLength == candyBasket.count { return maxLength }
        }
    }
    return maxLength
}
var answer = 1
for i in 0...(n - 1){
    for j in 0...(n - 1) {
        if i < n - 1 {
            swap((i, j), (i + 1, j))
            answer = max(answer, checkMaxLength(candyBasket))
            swap((i, j), (i + 1, j))
        }
        if j < n - 1 {
            swap((i, j), (i, j + 1))
            answer = max(answer, checkMaxLength(candyBasket))
            swap((i, j), (i, j + 1))
        }
        if answer == n { break }
    }
    if answer == n { break }
}
print(answer)
