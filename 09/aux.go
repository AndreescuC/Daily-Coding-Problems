package main

import "fmt"

func main() {
	for index, test := range getTests() {
		fmt.Printf("Test %d\nFor array %v test, solution: %d\n\n", index, test, solve(test))
	}
}

func getTests() [][]int {
	return [][]int{
		{5, 1, 1, 5},
		{2, 4, 6, 2, 5},
		{-1, 2, 3, -2, -15, -60, 60, 65, -58, 12, 45, 12, 12, 12, 0, 0, 44},
		{-1, -1},
		{0, 1, 2, 3, 4, 5, -12},
		{0, 1, 4, 3, 4, 7, -12},
	}
}
