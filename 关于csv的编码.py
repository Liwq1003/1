fr = open('score.csv','r')
ls = []
for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(","))
fr.close()

ls[0].append("总成绩")
for i in range(1, len(ls)):
    total = 0
    for j in range(1, len(ls[i])):
        total += int(ls[i][j])
    ls[i].append(str(total))
fw = open("newscore.csv","w")
for row in ls:
    fw.write(",".join(row) + "\n")
fw.close()
