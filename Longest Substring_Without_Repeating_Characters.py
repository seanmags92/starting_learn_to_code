class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_lenght = 1
        seen = []
        if len(s) <= 0:
            return 0

        for i in s:
            
            if i not in seen:
                seen.append(i)
                continue

            if i in seen:
                print(f'Seen {i} in {seen}')
                if len(seen) > max_lenght:
                    max_lenght = len(seen)
                new_seen = []
                while(len(seen)> 0):
                    new = seen.pop()
                    if new != i:
                        new_seen.append(new)
                    else:
                        break
                seen = new_seen[::-1]
                seen.append(i)


        if len(seen) >= max_lenght:
            return len(seen)
        return max_lenght

