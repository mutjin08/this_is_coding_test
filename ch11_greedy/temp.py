def solution(n, units):
    units.sort()

    target = 1
    for unit in units:
        if unit > target:
            return target
        target += unit
    
n = input()
units = list(map(int, input().split()))
print(solution(n, units))