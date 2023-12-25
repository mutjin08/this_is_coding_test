from heapq import heappush, heappop
def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    
    h = []
    for i in range(len(food_times)):
        heappush(h, (food_times[i], i+1))
    
    left_food = len(food_times)
    before = 0
    total = 0
    
    while total + (h[0][0]-before)*left_food <= k:
        now = heappop(h)[0]
        total += (now-before)*left_food
        
        before = now
        left_food -= 1
    
    last_cycle = sorted(h, key = lambda x : x[1])
    return last_cycle[(k - total)%left_food][1]