package main

func solve(n int) int {
	if n == 2 {
		return 1
	}

	if n%2 == 0 {
		return 2*solve(n/2) - 1
	}

	return f(n, solve(n/2+1))
}

func f(n int, pos int) int {
	if pos == 1 {
		return n
	}
	return 2*pos - 1
}
