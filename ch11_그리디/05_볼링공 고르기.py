from itertools import combinations
# from math import comb
def solution(n, m, weights):
    answer = 0
    for a, b in combinations(weights, 2):
        if a!=b:
            answer += 1

    return answer


n, m = map(int, input().split())
weights = list(map(int, input().split()))
print(solution(n, m, weights))