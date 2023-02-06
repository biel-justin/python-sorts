from Sorter import Sorter


class InsertionSorter(Sorter):
    def sort(self, nums: list):
        N = len(nums)
        for i in range(N):
            for j in range(i, 0, -1):
                if self.less(nums[j], nums[j - 1]):
                    self.swap(nums, j, j - 1)
        return nums


if __name__ == "__main__":
    t = [6, 9, 3, 3, 5, 0, 2]
    print(InsertionSorter().sort(t))
