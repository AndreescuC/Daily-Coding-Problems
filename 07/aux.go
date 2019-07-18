package main

import "fmt"

func main() {

	for index, test := range getTests() {
		fmt.Printf(
			"Test %d\nFor message %s, there are %d ways to decode it\n\n",
			index, test, solve(test),
		)
	}
}

func getTests() []string {
	return []string{
		"111",
		"261341",
		"1111",
		"1111111",
		"4",
		"34",
		"26",
		"201",
		"161203",
	}
}
