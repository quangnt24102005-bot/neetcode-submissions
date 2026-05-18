class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for i in strs:
            sort_word="".join(sorted(i))

            if sort_word not in seen:
                seen[sort_word]=[]

            seen[sort_word].append(i)
        return list(seen.values())
