class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        left_c = [0] * len(instructions)
        right_c = [0] * len(instructions)
        def merged(left_arr, right_arr):
            l = 0
            r = 0
            merge = []
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l][0] <= right_arr[r][0]:
                    merge.append(left_arr[l])
                    l += 1
                else:
                    merge.append(right_arr[r])
                    r += 1
            merge.extend(left_arr[l:])
            merge.extend(right_arr[r:])
            return merge
        def divided(l, r):
            if l == r:
                return [[instructions[l], l]]
            m = (l + r) // 2
            left = divided(l, m)
            right = divided(m + 1, r)
            lp = 0
            k = 0
            for val, i in right:
                while lp < len(left) and left[lp][0] < val:
                    lp += 1
                less = lp

                if k < lp:
                    k = lp
                    
                while k < len(left) and left[k][0] == val:
                    k += 1
                left_c[i] += less
                right_c[i] += (len(left) - k)
            return merged(left, right)
        divided(0, len(instructions) - 1)
        cost = 0
        mod = 10**9 + 7
        for i in range(len(left_c)):
            cost += min(left_c[i], right_c[i])

        return cost % mod