#!/bin/python3

import math
import os
import random
import re
import sys


#Given an array of integers, find the sum of its elements.For example, if the array ar = [1,2,3], 1+2+3 = 6 , so return 6.
#Function Description
#Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.
#simpleArraySum has the following parameter(s):
#ar: an array of integers
#Input Format
#The first line contains an integer, n, denoting the size of the array.
#The second line contains n space-separated integers representing the array's elements.
#Output Format  
#Print the sum of the array's elements as a single integer.

def simpleArraySum(ar):
    sum = 0
    for i in range(len(ar)):
        sum += ar[i]
    return sum



#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    score_a = 0 
    score_b = 0
    for i in range(3):
        if a[i] > b[i]:
            score_a += 1
        elif a[i] < b[i]:
            score_b += 1
    return [score_a, score_b]


#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    sum = 0
    for i in range(len(ar)):
        sum += ar[i]
    return sum


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here