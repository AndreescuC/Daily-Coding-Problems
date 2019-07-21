package main

import "fmt"

func main() {

	for index, test := range getTests() {
		fmt.Printf("Test %d, result: %d\n", index, solve(&test))
	}
}

func getTests() []TreeNode {
	return []TreeNode{
		// Test 1
		TreeNode{
			value: 0,
			left: &TreeNode{
				value: 1,
				left:  nil,
				right: nil,
			},
			right: &TreeNode{
				value: 0,
				left: &TreeNode{
					value: 1,
					left: &TreeNode{
						value: 1,
						left:  nil,
						right: nil,
					},
					right: &TreeNode{
						value: 1,
						left:  nil,
						right: nil,
					},
				},
				right: &TreeNode{
					value: 0,
					left:  nil,
					right: nil,
				},
			},
		},

		// Test 2
		TreeNode{
			value: 1,
			left:  nil,
			right: nil,
		},

		// Test 3
		// 	    1
		// 	  2   5
		// 	 3      4
		//	4     2
		// 5    2    2
		//     2 2  2 2
		TreeNode{
			value: 1,
			left: &TreeNode{
				value: 2,
				left: &TreeNode{
					value: 3,
					left: &TreeNode{
						value: 4,
						left: &TreeNode{
							value: 5,
							left:  nil,
							right: nil,
						},
						right: nil,
					},
					right: nil,
				},
				right: nil,
			},
			right: &TreeNode{
				value: 5,
				left:  nil,
				right: &TreeNode{
					value: 4,
					left: &TreeNode{
						value: 2,
						left: &TreeNode{
							value: 2,
							left: &TreeNode{
								value: 2,
								left:  nil,
								right: nil,
							},
							right: &TreeNode{
								value: 2,
								left:  nil,
								right: nil,
							},
						},
						right: &TreeNode{
							value: 2,
							left: &TreeNode{
								value: 2,
								left:  nil,
								right: nil,
							},
							right: &TreeNode{
								value: 2,
								left:  nil,
								right: nil,
							},
						},
					},
					right: nil,
				},
			},
		},

		// Test 4
		// 	    1
		// 	  2   5
		// 	 3      4
		//	4     2
		// 5    2    2
		//     1 1  1 1
		TreeNode{
			value: 1,
			left: &TreeNode{
				value: 2,
				left: &TreeNode{
					value: 3,
					left: &TreeNode{
						value: 4,
						left: &TreeNode{
							value: 5,
							left:  nil,
							right: nil,
						},
						right: nil,
					},
					right: nil,
				},
				right: nil,
			},
			right: &TreeNode{
				value: 5,
				left:  nil,
				right: &TreeNode{
					value: 4,
					left: &TreeNode{
						value: 2,
						left: &TreeNode{
							value: 2,
							left: &TreeNode{
								value: 1,
								left:  nil,
								right: nil,
							},
							right: &TreeNode{
								value: 1,
								left:  nil,
								right: nil,
							},
						},
						right: &TreeNode{
							value: 2,
							left: &TreeNode{
								value: 1,
								left:  nil,
								right: nil,
							},
							right: &TreeNode{
								value: 1,
								left:  nil,
								right: nil,
							},
						},
					},
					right: nil,
				},
			},
		},
	}
}
