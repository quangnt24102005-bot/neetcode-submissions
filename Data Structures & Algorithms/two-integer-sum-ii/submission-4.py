class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        trai=0
        phai=len(numbers)-1

        while trai<phai:
            tong=numbers[trai]+numbers[phai]
            if tong==target:
                return [trai+1,phai+1]
            elif tong<target:
                trai+=1
            else:
                phai-=1
        
