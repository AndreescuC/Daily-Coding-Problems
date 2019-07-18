package main

func solve(message string) int {
	var pos = make([]int, len(message))
	var current_pos int = 1

	for index, char := range message {
		if char == '0' {
			pos[index] = 0
			continue
		}
		if index < len(message) - 1 && message[index:index + 1] < "27" {
			current_pos ++
		}
		pos[index] = current_pos
		current_pos = 1
	}

	var branches = []int{1, 0}
	var aux int
	for index, options := range pos {

		if index < len(pos) - 1 && pos[index + 1] == 0 {
			branches[1] = 0
		}

		switch options {
		case 2:
			aux = branches[1]
			branches[1] = branches[0]
			branches[0] += aux
		case 1:		
			branches[0] += branches[1]
			branches[1] = 0
		case 0:
			branches[1] = 0
		default:
			panic("Illegal options size")
		}

	}

	return branches[0]
}
