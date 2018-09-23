'''
题目描述：
小明有50元、20元、10元、5元、1元的任意数量的零钱，问给定一个数值的金额，有多少种零钱的组合方式？
输入：10
输出：4
通过率：80%
'''
#coding=utf-8
import sys
n = int(raw_input())
l = [50, 20, 10, 5, 1]
r = 0
def func(n, l):
    global r
    if n == 0:
        r += 1
    for i in range(len(l)):
        if n >= l[i]:
            func(n - l[i], l[i:])
func(n, l)
print r
