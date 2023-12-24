def solution(s):
    s = list(map(int, s))
    to_0, to_1 = 0, 0

    if s[0]==0:
        to_1 += 1
    elif s[0]==1:
        to_0 += 1

    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            if s[i+1]==0:
                to_1 += 1
            elif s[i+1]==1:
                to_0 += 1
    
    return min(to_0, to_1)


s = input()
print(solution(s))