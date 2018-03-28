# add your code here
import re

line = []

n = int(input())


for i in range(n):
	singleLine = input()
	singleList = re.findall(r"[\w]+|[^\s\w]", singleLine)
	for j in range(len(singleList)):
		if singleList[j].isalnum():
			line.append(singleList[j])

#print(line)
numLine = []

for a in range(len(line)):
	counter = 0
	sameEx = False
	for b in range(a, len(line)):
		if a != b:
			if line[a] == line[b]:
				sameEx = True
				numLine.append(b-a-1)
				break
	if not sameEx:
		numLine.append(0)
print(' '.join(str(numLine[x]) for x in range(len(numLine))))
