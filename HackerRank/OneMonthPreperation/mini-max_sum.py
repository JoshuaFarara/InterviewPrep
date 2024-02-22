'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of  integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

Input Format

A single line of five space-separated integers.

Constraints


Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

The numbers are , , , , and . Calculate the following sums using four of the five integers:

Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Hints: Beware of integer overflow! Use 64-bit Integer.

Need help to get started? Try the Solve Me First problem

'''

# Methodology for Solving
'''
MAIN Objective: summing exactly four of the five integers
1. Must loop through the array to access and analyze each element
    1.1 - recall array indexing starts from 0, and len(arr) is the total elements within that array
2. This requirement means that any of the 4 integers in the array, have a sum that will be the minimum and maximum = meaning slicing will be necessary
    2.1 - arr[:i]: This slices the array arr from the beginning up to (but not including) the index i, effectively excluding the ith element.
    2.2 - arr[i+1:]: This slices the array arr from the index i+1 till the end, effectively excluding the ith element as well. 
          This allows you to extract a portion of the array starting from a specified index till the end.

'''

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def main():
    arr = [1, 2, 3, 4, 5]
    arr2 = [7, 69, 2, 221, 8974]
    # print(arr[])
    
    # miniMaxSum(arr)
    miniMaxSum2(arr2)
    # miniMaxSum(arr

#attempt number one
def miniMaxSum(arr):
    
    minSum = 0
    maxSum = 0

    for n in range(0,4):
        minSum += arr[n]
    for n in range(1,5):
        maxSum += arr[n]

    print(minSum, maxSum)

# attempt number two
def miniMaxSum2(arr):
    
    minSum = sum(arr[:4])
    maxSum = sum(arr[:4])

    for n in range(len(arr)):
        current_sum = sum(arr[:n] + arr[n+1:])
        if current_sum < minSum:
            minSum = current_sum
        if current_sum > maxSum:
            maxSum = current_sum

    print(minSum, maxSum)


if __name__ == '__main__':

    # arr = list(map(int, input().rstrip().split()))

    # miniMaxSum(arr)
    main()
