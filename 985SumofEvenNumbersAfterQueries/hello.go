package main

import "fmt"

func sumEvenAfterQueries(nums []int, queries [][]int) []int {
	var idx, val int
	var answer []int
	var sumSoFar int = 0
	for _, value := range nums {
		if value%2 == 0 {
			sumSoFar += value
		}
	}
	for _, element := range queries {
		idx = element[1]
		val = element[0]
		if nums[idx]%2 == 0 {
			sumSoFar -= nums[idx]
		}
		nums[idx] += val

		if nums[idx]%2 == 0 {
			sumSoFar += nums[idx]
		}
		answer = append(answer, sumSoFar)
	}
	return answer
}

func main() {
	nums := []int{1, 2, 3, 4}
	queries := [][]int{{1, 0}, {-3, 1}, {-4, 0}, {2, 3}}
	t := sumEvenAfterQueries(nums, queries)
	fmt.Println(t)
	fmt.Println("Hello, World!")
}
