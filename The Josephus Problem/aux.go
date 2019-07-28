package main

import "fmt"

func main() {
	for index, test := range getTests() {
		fmt.Printf(
			"Test %d. For %d people, the safe position is at %d\n",
			index,
			test,
			solve(test),
		)
	}
}

func getTests() []int {
	return []int{
		2, 3, 4, 5, 8, 256, 1024, 255, 20, 21, 50, 51, 500,
	}
}
