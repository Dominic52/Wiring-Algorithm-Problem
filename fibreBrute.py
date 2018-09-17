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
        total = int(line[i])
        if total > maxprofit:
            maxprofit = total
        for j in range(i+1, len(line)):
            total = total + int(line[j])
            if total > maxprofit:
                maxprofit = total

    print(maxprofit)
