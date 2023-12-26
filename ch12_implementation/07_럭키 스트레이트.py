def solution(n):
    nums = []
    while n>0:
        nums.append(n%10)
        n//=10
    
    length = len(nums)
    if sum(nums[:length//2]) == sum(nums[length//2:]):
        return "LUCKY"
    else:
        return "READY"

n = int(input())
print(solution(n))