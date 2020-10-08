from typing import List
import pytest

class Solution:
    rotate = 0
    lenth = 0
    def normalize(self, pos:int) -> int:
        return (pos+self.rotate) % self.lenth
    def search(self, nums: List[int], target: int) -> int:
        self.lenth = len(nums)
        self.rotate = self.rotate(nums)
        print(f'{self.lenth=},{self.rotate=}')
        start=0;
        end = self.lenth-1
        while start<=end:
            print(f'{start=}, {end=}')
            mid = (start+end)//2
            mval = nums[self.normalize(mid)]
            print(f'  {mid=}, {mval=}, {target=}')
            if mval > target:
                end = mid - 1
            elif mval < target:
                start = mid + 1
            else:
                return self.normalize(mid)

        return -1
    def rotate(self,nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while end>start:
            print(f'in rotate: {end=}, {start=}')
            if nums[start] > nums[end]:
                mid = (start+end)//2
                if nums[mid] > nums[start]:
                    start = mid
                elif nums[mid] < nums[end]:
                    end = mid

                else:
                    return end
            else:
                return start
        return end


@pytest.mark.parametrize("nums,target,output", [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([6,7,0,1,2,4,5], 3, -1),
    ([1,3], 1, 0),
    ([3,1], 1, 1),
    ([1,3], 0, -1),
])
def test_eval(nums, target, output):
    solution = Solution()
    ret = solution.search(nums,target)

    print(f'{nums=},{target=},{ret=}, {output=}')
    assert ret == output

def get_rotate(nums):
    print()
    solution = Solution()
    ret = solution.rotate(nums)
    print(f'{nums=}, {ret=}')

def atest_rotate():
    get_rotate([4, 5, 6, 7, 0, 1, 2])
    get_rotate([5, 6, 7, 0, 1, 2, 3, 4])
    get_rotate([0, 1, 2, 4, 6, 7])
    get_rotate([7, 0, 1, 2, 3, 4, 5, 6, ])
    get_rotate([3,1])
    get_rotate([1, 3])


if __name__ == "__main__":
    solution = Solution()

    nums = [1,3]
    tartget = 0
    ret = solution.search(nums,tartget)
    print(f'{nums=}, {ret=}')

    #atest_rotate()

    mock = 0