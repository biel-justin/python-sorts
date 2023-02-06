from Sorter import Sorter


class SelectionSorter(Sorter):
    def sort(self, nums: list):
        N = len(nums)
        for i in range(N - 1):
            min_idx = i
            for j in range(i + 1, N):
                if self.less(nums[j], nums[min_idx]):
                    min_idx = j
            self.swap(nums, i, min_idx)
        return nums


if __name__ == "__main__":
    t = [6, 1, 3, 3, 5, 0, 9]
    print(SelectionSorter().sort(t))
