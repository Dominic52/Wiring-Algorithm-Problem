import sys
run = True
while run:
    # Reads input
    lines = sys.stdin.readline()
    # Formats into list of values
    line = lines.strip().split(' ')
    # Ends input read
    if len(line) == 1:
        break

    maxprofit = 0

    for i in range(len(line)):
        for j in range(1, len(line)):
            total = 0
            for k in range(i, j+1):
                total = total+int(line[k])
            if total > maxprofit:
                maxprofit = total

    print(maxprofit)
