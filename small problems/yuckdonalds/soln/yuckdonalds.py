import sys
sys.setrecursionlimit(30000)
# the above recursion limit should be sufficient to solve the problem
# add your code below
first_ln = input().split()
M = input().split()
for i in range(len(M)):
    M[i] = int(M[i])
P = input().split()
for j in range(len(P)):
    P[j] = int(P[j])
n = int(first_ln[0])
k = int(first_ln[1])

def maxprofits():
    count = [0]*n
    count [0] = P[0]
    result = 0
    for i in range(1,n):
        count[i] = P[i]
        for j in range(i-1,-1,-1):
            if M[i]-M[j] >= k:
                max_p = count[j]+P[i]
                count[i] = max(max_p,count[i])
                tem_result = max(max_p,count[i])
                result = max(result,tem_result)
                break
            else:
                count[i] = max(count[i],count[j])
                result = max(result,count[i])
    return result
print(maxprofits())
