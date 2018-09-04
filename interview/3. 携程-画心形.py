#-*-coding"utf-8-*-
'''
应聘职位：数据分析师
题目描述：
输入为一行四个数，代表两点坐标(lx, ly) (rx, ry),ex:2 3 2 7
根据输入指定的两点在10*10的矩阵中按照规则画出心形形状，心的部位用'#'表示，其它位置用'-'表示。
下面的答案只有50%的通过率，未通过输入示例1 7 1 13.
'''
import sys

def heart():
    lpx, lpy, rpx, rpy = sys.stdin.readline().split()
    output = [['#' for j in range(10)] for i in range(10)]
    lpx, lpy, rpx, rpy = int(lpx) - 1, int(lpy) - 1, int(rpx) - 1, int(rpy) - 1
    if lpy > rpy:
        lpy, rpy = rpy, lpy
    bottomx = 2 * (rpy - lpy - 1) + lpx
    y = lpy + (rpy - lpy) / 2
    if (rpy - lpy) % 2 == 0:
        bottom_lefty = bottom_righty = y
    else:
        bottom_lefty, bottom_righty = y, y + 1
    print bottomx, bottom_lefty, bottom_righty
    for i in range(10):
        if i < lpx or i > bottomx:
            output[i][:] = ['-'] * 10
            continue
        for j in range(10):
            if j <= lpy and (lpy - j) > (i - lpx):
                output[i][j] = '-'
            elif j >= rpy and (j - rpy) > (i - rpx):
                output[i][j] = '-'
            elif i <= bottomx and (bottom_lefty - j) > (bottomx - i):
                output[i][j] = '-'
            elif i <= bottomx and (j - bottom_righty) > (bottomx - i):
                output[i][j] = '-'
            elif lpy < j < rpy and ((j - lpy) > (i - lpx) and (rpy - j) > (i - rpx)):
                output[i][j] = '-'
    for i in range(10):
        for j in range(10):
            print output[i][j], 
        print 

if __name__ == "__main__":
    heart()
