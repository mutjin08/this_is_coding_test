def solution(n, units):
    units.sort()

    target = 1
    for unit in units:
        if target < unit:
            return target
        target += unit

n = int(input())
units = list(map(int, input().split()))
print(solution(n, units))