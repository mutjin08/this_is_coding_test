def solution(s):
    answer = []
    total = 0
    for c in s:
        if c.isalpha():
            answer.append(c)
        else:
            total += int(c)
    
    answer.sort()

    #주의
    if total > 0:
        answer.append(str(total))

    return "".join(answer)


s = input()
print(solution(s))