from Sorter import Sorter


class BubbleSorter(Sorter):
    def sort(self, nums: list):
        N = len(nums)
        isSorted = False
        while not isSorted:
            isSorted = True
            for i in range(N - 1):
                if self.less(nums[i + 1], nums[i]):
                    isSorted = False
                    self.swap(nums, i, i + 1)
        return nums


if __name__ == "__main__":
    t = [6, 1, 3, 3, 5, 0, 9]
    print(BubbleSorter().sort(t))
