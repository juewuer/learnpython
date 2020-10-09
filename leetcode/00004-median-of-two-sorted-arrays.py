from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2,nums1
            print(nums1,nums2)
        len1=len(nums1)
        len2=len(nums2)
        if len1+len2 == 0:
            return 0
        target = (len1+len2+1)//2
        i1 = -1 + (len1-len2+1)//2
        i2 = -1
        ind = -1;
        while i1+i2+2<target and i2+1 < len2:

            if nums1[i1+1]>nums2[i2+1]:
                i2 += 1
                ind =1
            else:
                i1 += 1
                ind=0

        if i1+i2+2<target:
            ind = 0
            i1=target-2-i2
        if i1<0 or( i2>=0 and  nums1[i1] < nums2[i2]):
            median = nums2[i2]
        else:
            median = nums1[i1]
        print( f'  {nums1}, {nums2},{len1=} {len2=} {i1=} {i2=} {ind=} {target=} {median=}'  )
        if (len1+len2)%2==0:
            if i1+1>=len1 or (i2+1<len2 and nums2[i2+1]<nums1[i1+1]):
                median += nums2[i2+1]
            else:
                median += nums1[i1+1]
            median /= 2

            print( f'     {nums1}, {nums2}, {nums1[i1]} {nums2[i2]},{i1=} {i2=} {ind=} {target=}'  )
        print(f'{median=}')
        return median

import pytest
import math
import sys
if __name__=="__main__":
    s = Solution()
    mock = 0

    nums1 = [3]
    nums2 = [2]
    out = 2.5000
    out = 1.00000  if mock else out
    assert math.isclose(s.findMedianSortedArrays(nums1, nums2), out)


    nums1 = [1]
    nums2 = [2,3]
    out = 2.0000
    out = 1.00000  if mock else out
    assert math.isclose(s.findMedianSortedArrays(nums1, nums2), out)

    nums1 = []
    nums2 = [1,2,3,4,5]
    out = 3.0000
    out = 1.00000  if mock else out
    assert math.isclose(s.findMedianSortedArrays(nums1, nums2), out)
    #sys.exit(1)

    nums1 = [1,3,5,8]
    nums2 = [2,4,6,7]
    out = 4.50000
    out = 1.00000  if mock else out
    assert math.isclose(s.findMedianSortedArrays(nums1, nums2), out)

    nums1 = [1,2]
    nums2 = [3,4]
    out = 2.50000

    out = 1.00000 if mock else out
    assert math.isclose(s.findMedianSortedArrays(nums1, nums2), out)

    nums1 = []
    nums2 = [1]
    out = 1.00000
    assert math.isclose(s.findMedianSortedArrays(nums1, nums2), out)

    nums1 = [2]
    nums2 = []
    out = 2.00000
    out = 1.00000  if mock else out
    assert math.isclose(s.findMedianSortedArrays(nums1, nums2), out)
