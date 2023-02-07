from Sorter import Sorter


class ShellSorter(Sorter):
    def sort(self, nums: list):
        N = len(nums)
        h = 1
        while h < N / 3:
            h = 3 * h + 1

        while h >= 1:
            for i in range(h, N):
                for j in range(i, h - 1, -h):
                    if self.less(nums[j], nums[j - h]):
                        self.swap(nums, j, j - h)
                    else:
                        break
            h = h // 3
        return nums


if __name__ == "__main__":
    t = [6, 9, 3, 3, 5, 0, 2]
    print(ShellSorter().sort(t))
