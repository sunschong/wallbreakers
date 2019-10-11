class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        #find max in list and return index
        mid =  len(A) // 2
        start = 0
        end = len(A) - 1
        peak = 0
        while start <= mid and end >= mid:
            print(mid)
            if A[mid - 1] < A[mid] > A[mid + 1]:
                return mid
            if A[mid + 1] > A[mid]:    
                start = mid + 1
            else:
                end = mid - 1
            mid = (end + start) // 2
    
        return peak