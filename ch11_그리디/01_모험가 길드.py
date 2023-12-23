def solution(n, afs):
    group, member = 0, 0
    afs.sort()

    for af in afs:
        member += 1
        if member >= af:
            group += 1
            member = 0
    
    return group

n = int(input())
afs = list(map(int, input().split()))
print(solution(n, afs))