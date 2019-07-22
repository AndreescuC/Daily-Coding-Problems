package main

func max(args ...int) int {
	max := args[0]
	for _, x := range args {
		if x > max {
			max = x
		}
	}
	return max
}

func solve(v []int) int {
	posibilities := [3]int{0, 0, 0}
	var aux int

	for _, element := range v {
		if element > 0 {
			aux = posibilities[2]
			posibilities[2] = max(posibilities[1], posibilities[0]) + element
			posibilities[0] = posibilities[1]
			posibilities[1] = aux
		} else {
			posibilities[0] = max(posibilities[1], posibilities[2])
			posibilities[1] = posibilities[0]
			posibilities[2] = 0
		}
	}

	return max(posibilities[0], posibilities[1], posibilities[2])
}
