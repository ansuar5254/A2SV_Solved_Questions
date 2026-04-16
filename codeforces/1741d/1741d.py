def merged(left_arr, right_arr):
    if max(left_arr) <= min(right_arr):
        pass
    elif min(left_arr) >= max(right_arr):
        op[0] += 1
    else:
        imposible[0] = 1

    l = 0
    r = 0
    merge = []

    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] <= right_arr[r]:
            merge.append(left_arr[l])
            l += 1
        else:
            merge.append(right_arr[r])
            r += 1

    merge.extend(left_arr[l:])
    merge.extend(right_arr[r:])
    return merge
def divided(left,right):
    if left == right:
        return [a[left]]
    mid = (left + right)//2
    left_half = divided(left,mid)
    right_half = divided(mid+1,right)

    return merged(left_half,right_half)

t =int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    op = [0]
    imposible = [0]
    divided(0,n-1)
    if imposible[0] == 1:
        print(-1)
    else:
        print(op[0])