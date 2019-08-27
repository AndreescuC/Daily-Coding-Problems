package main

import "fmt"

func main() {
	for index, test := range getTests() {
		fmt.Printf(
			"Test %d: given %s\nAnswer: %d\n\n",
			index,
			test,
			solve(test),
		)
	}
}

func getTests() []string {
	return []string{
		"()",
		"(()(()))()",
		"()(()()",
		"()(()())",
		"())())()())()()()))",
		")))))(((((",
	}
}
