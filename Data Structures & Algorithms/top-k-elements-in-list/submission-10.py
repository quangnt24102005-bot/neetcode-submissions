class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst=[]
        lst_set=list(set(nums))
        for i in lst_set:
            x=nums.count(i)
            lst.append([x,i])
        lst.sort(reverse=True)
        print(lst)
        lst_k=lst[0:k]
        return [x[1] for x in lst_k]
            



