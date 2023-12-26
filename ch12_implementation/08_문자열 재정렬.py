def solution(s):
    answer = []
    total = 0
    for i in s:
        if i.isalpha():
            answer.append(i)
        else:
            total += int(i)
    
    #주의
    if total>0:
        answer.append(str(total))

    return "".join(answer)

s = input()
print(solution(s))