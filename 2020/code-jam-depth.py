cases = int(input())
for case in range(0,cases):
    line = input()
    newLine = "(" * int(line[0])
    newLine += line[0]
    for i in range(1, len(line)):
        dif = int(line[i])-int(line[i-1])
        if dif > 0:
            newLine+= "(" * dif
        elif dif< 0:
            newLine += ")" * (dif * -1)
        newLine += line[i]
    newLine += ")" * int(line[len(line)-1])
    print(f"Case #{case+1}: {newLine}")
