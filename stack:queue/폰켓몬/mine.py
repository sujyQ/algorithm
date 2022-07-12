def solution(nums):
    type_set = set()
    for num in nums :
        type_set.add(num)
    return len(type_set) if len(type_set) < len(nums)//2 else len(nums)//2