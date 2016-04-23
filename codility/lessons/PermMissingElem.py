# Task description and code solution correctness and performance analysis: https://codility.com/demo/results/demo9RDK95-8NE/

# A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

# Your goal is to find that missing element.

def solution(A):
    full_A_length = len(A) +1
    sum_all = (full_A_length**2 + full_A_length) / 2  	# sum of all integers 1,2,...,n-1,n
    return sum_all - sum(A)								# integer number missing from the list


assert solution([2, 3, 1, 5]) == 4