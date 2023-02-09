from Sorter import Sorter


class MergeSorter(Sorter):
    def sort(self, nums: list):
        N = len(nums)
        if N <= 1:
            return nums
        mid = N // 2
        left = nums[:mid]
        right = nums[mid:]

        self.sort(left)
        self.sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        return nums


if __name__ == "__main__":
    t = [6, 9, 3, 3, 5, 0, 2]
    print(MergeSorter().sort(t))
