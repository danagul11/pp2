def even_num(a):
    ans = []
    for i in a:
        if i % 2 == 0:
            ans.append(i)
    return ans
nums = list(map(int, input().split()))
print(even_num(nums))