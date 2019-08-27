package main

import "fmt"

type stack struct {
	st []int
}

func (st *stack) push(element int) {
	st.st = append(st.st, element)
}

func (st *stack) pop() int {
	n := len(st.st) - 1
	element := st.st[n]
	st.st = st.st[:n]
	return element
}

func (st *stack) peek() int {
	return st.st[len(st.st)-1]
}

func (st *stack) isEmpty() bool {
	return len(st.st) == 0
}

func (st *stack) String() string {
	s := ""
	for i := len(st.st) - 1; i >= 0; i-- {
		s += fmt.Sprintf("%d ", st.st[i])
	}
	return s + "\n"
}

func solve(input string) int {
	var last, best int = 0, 0
	st := &stack{}
	st.push(-1)

	for index, p := range input {
		if p == '(' {
			st.push(index)
		} else {

			st.pop()
			if st.isEmpty() {
				st.push(index)
			} else {
				last = index - st.peek()
				if last > best {
					best = last
				}
			}
		}
	}

	if last > best {
		best = last
	}

	return best
}
