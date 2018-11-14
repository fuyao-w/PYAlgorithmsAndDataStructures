# -*- coding: UTF-8 -*-
def swap(arr, a, b):
    t = arr[a]
    arr[a] = arr[b]
    arr[b] = t


def heapAdjust(arr, index):
    left, right = index * 2 + 1, index * 2 + 2
    if left < len(arr) and arr[left][0] > arr[index][0]:
        swap(arr, left, index)
        heapAdjust(arr, left)
    if right < len(arr) and arr[right][0] > arr[index][0]:
        swap(arr, right, index)
        heapAdjust(arr, right)


def buildHeap(arr):
    lastIndex = int(len(arr) / 2)
    for i in range(lastIndex):
        index = lastIndex - 1 - i
        heapAdjust(arr, index)


def heapSort(arr, k):
    buildHeap(arr)
    res = []
    for i in range(k):
        t = len(arr) - i - 1
        swap(arr, 0, len(arr) - 1)
        res.append(arr.pop()[1])
        heapAdjust(arr, 0)
    return res


def sortCount(nums, min, max):
    '''
    计数排序：
    思想：首先需要知道这个数组中的最大值和最小值分别是多少
    然后维护一个 max-min+1的数组 用于保存 索引位置数-min 在待排序数组里的每一个数字数组出现的此时
    辅助数组索引就是待排序数组每个数字按大小顺序排列出现的次数了
    然后通过辅助数组来重新构建
    数组的索引加上最小值就是原数组的数字
    :param nums: 待排序数组
    :param min: 数组中的最小值
    :param max: 数组中的最大值
    :return:
    '''
    tmp = [0 for i in range(max - min + 1)]
    for i in nums:
        tmp[i - min] += 1
    q = 0
    for i in range(len(tmp)):
        while tmp[i] > 0:
            nums[q] = i
            q += 1
            tmp[i] -= 1

    print(nums)


def topKFrequent(nums, k):
    '''
    给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
    你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
    你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
    思路：用堆排序和hash(字典)来解决
    先用一个字典记录每个元素出现的次数
    再将 字典的val key转换成数组
    用堆排序 输出 出现次数前k的key值
    :param nums:
    :param k:
    :return:
    '''
    r = {}
    for i in nums:
        if r.get(i) is None:
            r[i] = 1
        else:
            r[i] += 1
    # d = []
    # for key, val in r.items():
    #     d.append((val, key))
    # return heapSort(d, k)
    arry = [[num, r[num]] for num in r]
    arry = sorted(arry, key=lambda item: 0 - item[1])
    r = map(lambda item: item[0], arry)
    return list(r)[:k]


def findPeakElement(nums):
    '''
    峰值元素是指其值大于左右相邻值的元素。

    给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

    数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

    你可以假设 nums[-1] = nums[n] = -∞。
    >>> findPeakElement([1, 2])
    :param self:
    :param nums:
    :return:
    '''
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) / 2
        if mid == len(nums) - 1:
            return mid
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return right


def searchRange(nums, target):
    '''
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

    你的算法时间复杂度必须是 O(log n) 级别。(二分法)

    如果数组中不存在目标值，返回 [-1, -1]。
    :param nums:
    :param target:
    :return:
    '''
    left, right = 0, len(nums) - 1
    flag = True
    mid = int((left + right) / 2)
    while left <= right:

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            flag = False
            break
        mid = int((left + right) / 2)
    if flag:
        return [-1, -1]
    left = right = mid
    while left >= 0 and nums[left] == nums[mid]:
        left -= 1
    while right < len(nums) and nums[right] == nums[mid]:
        right += 1
    return [left + 1, right - 1]


if __name__ == '__main__':
    print(searchRange([2],
                      2))
    # arr = [1, 1, 1, 2, 2, 3]
    # heapSort(arr)
