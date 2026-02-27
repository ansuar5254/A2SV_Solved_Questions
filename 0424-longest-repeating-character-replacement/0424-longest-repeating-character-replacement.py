class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_w = 0
        left = 0
        freq_counter = defaultdict(int)
        for right in range(n):
            freq_counter[s[right]] += 1
            while (right - left + 1) - max(freq_counter.values()) > k:
                freq_counter[s[left]] -= 1
                left += 1
            max_w = max(max_w, right - left + 1)
        return max_w