def pivotIndex(nums):
    l = 0
    r = sum(nums)

    for i in range(len(nums)):
        r -= nums[i]
        if l == r:
            print(nums[i])
        l += nums[i]

    print(-1)

pivotIndex([3, 2, 3, 8, 4, 4])
