# add your code here
m = int(input())

line = list(map(int, input().split()))

visited = [0]*len(line)
if m == 0:
	print(' '.join(str(1) for x in range(len(line))))
else:
	for i in range(len(line)):
		critical = m
		out = 0
		for j in range(i, len(line)):
			critical = critical-line[j]
			out += 1
			if critical <= 0:
				find = True
				visited[i] = out
				break
	print(' '.join(str(visited[x]) for x in range(len(visited))))
