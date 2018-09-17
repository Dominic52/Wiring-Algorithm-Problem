import sys


def DC(arr, length):
    if len(arr) == 1:
        return int(arr[0])
    halflen = length//2

    sum = 0
    leftintermax = 0
    for i in range(halflen-1, -1, -1):
        sum = sum + int(arr[i])
        if sum > leftintermax:
            leftintermax = sum

    sum = 0
    rightintermax = 0
    for i in range(halflen, length):
        sum = sum + int(arr[i])
        if sum > rightintermax:
            rightintermax = sum

    leftmax = DC(arr[0:halflen], halflen)
    rightmax = DC(arr[halflen:], length-halflen)
    intermax = leftintermax + rightintermax

    largerside = max(leftmax, rightmax)
    return max(largerside, intermax)


run = True
while run:
    line = sys.stdin.readline()
    line = line.strip().split(' ')
    if len(line) == 1:
        break
    else:
        length = len(line)
        print(DC(line, length))
