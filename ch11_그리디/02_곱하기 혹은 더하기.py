def solution(s):
    s = list(map(int, s))

    result = s[0]
    for i in range(1, len(s)):
        # 주의 : 0뿐만 아니라 1일때도 더하기가 유리하다
        if result<=1 or s[i]<=1:
            result += s[i]
        else:
            result *= s[i]

    return result

s = input()
print(solution(s))