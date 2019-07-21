package main

func solve(t *TreeNode) int {
	trees, _ := count(t)
	return trees
}

func count(t *TreeNode) (int, bool) {
	if t == nil {
		return 0, false
	}

	if t.left == nil && t.right == nil {
		return 1, true
	}

	leftCount, leftUnival := count(t.left)
	rightCount, rightUnival := count(t.right)

	count := rightCount + leftCount
	unival := leftUnival && rightUnival

	if t.left != nil {
		unival = unival && (t.left.value == t.value)
	}

	if t.right != nil {
		unival = unival && (t.right.value == t.value)
	}

	if unival {
		count++
	}

	return count, unival
}
