import Foundation
var num = Int(readLine()!)!
var arr: [Bool] = Array(repeating: true, count: 10000000 + 1)
var answer: [Int] = []
var k: Int = 2

while (num != 1) {
	if (num % k == 0) {
		print(k)
		num /= k
	} else {
		k += 1
	}
}
answer.reverse()
for i in answer {
    print(i)
}
