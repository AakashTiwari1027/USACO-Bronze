#Silver
import sys
sys.stdin = open('moobuzz.in','r')
sys.stdout = open('moobuzz.out','w')
n = int(input())

moobuzz = [1,2,4,7,8,11,13,14]

# 1 2 3 1 3 2 1 2 1 2 3 1 3 2 1 2 1 2 3 1 3 2 1 2 1 2 3
#[1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44, 46, 47, 49]
#diff array is repeating 1 2 3 1 3 2 1 2

#fizz buzz sequence is 1 2 3 7 8 11 13 14, and then all terms after are +15

print(moobuzz[(n%8)-1]+(15*(n//15)))