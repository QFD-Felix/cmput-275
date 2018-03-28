# add your solution here
n = int(input())

memo = {}
highest = 0
for i in range(n):
	level = int(input())
	if level not in memo:
		memo[level] = 1
		highest = max(level,highest)
	else:
		memo[level] += 1

total = n
for i in range(1,highest+1):
	print(total)
	if i  in memo:
		total -= memo[i]
