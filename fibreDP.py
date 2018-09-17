import sys

run = True
while run:
    line = sys.stdin.readline()
    line = line.strip().split(' ')
    if len(line) == 1:
        break
    else:
        total = 0
        maximum = 0

        for i in range(len(line)):
            total = total + int(line[i])
            if total > maximum:
                maximum = total

            if total < 0:
                total = 0

        print(maximum)
