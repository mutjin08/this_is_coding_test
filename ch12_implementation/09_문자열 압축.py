def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        compressed = ""
        flag = s[0:step]
        repeat = 1
        for i in range(step, len(s), step):
            if s[i:i+step]==flag:
                repeat+=1
            else:
                if repeat > 1:
                    compressed += str(repeat)+flag
                else:
                    compressed += flag
                flag = s[i:i+step]
                repeat = 1
        if repeat > 1:
            compressed += str(repeat)+flag
        else:
            compressed += flag
        if answer > len(compressed):
            answer = len(compressed)
    return answer