n = int(input())
for i in range(n):
    nums = input().split()
    x,y,z,g = int(nums[0]),int(nums[1]),int(nums[2]),int(nums[3])
    if x==y and y==z and z == g:
        print("yes")
    else:
        print('no')
        