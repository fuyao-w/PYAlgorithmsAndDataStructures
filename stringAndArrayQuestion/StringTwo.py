# -*- coding: UTF-8 -*-
import collections
from copy import deepcopy


def threeSum(nums):
    '''
    三数之和
    先排顺序，然后遍历
    :param nums:
    :return:
    '''
    nums.sort()
    print(nums)
    result = []
    if len(nums) <= 2:
        return result
    for x in range(len(nums)):
        if nums[x] > 0:
            break
        elif x > 0 and nums[x] == nums[x - 1]:
            continue
        i = x + 1
        j = len(nums) - 1

        while i < j:
            res = []
            res.append(nums[x])
            if nums[i] + nums[j] > -nums[x]:
                j -= 1
            elif nums[i] + nums[j] < -nums[x]:
                i += 1
            elif nums[i] + nums[j] == -nums[x]:
                res.append(nums[i])
                res.append(nums[j])

                while i < j and nums[i] == nums[i + 1]: i += 1
                while i < j and nums[j] == nums[j - 1]: j -= 1
                i += 1
                j -= 1
                if len(res) > 1:
                    result.append(res)

    return result

def threeSumClosest(nums, target):
    '''
    最接近的三数之和
    与三数值和思路差不多
    但是要注意的是tmp需要与target比较
    :param nums:
    :param target:
    :return:
    '''
    res = 10000000
    nums.sort()
    r = 0
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while right > left:
            tmp = nums[i] + nums[left] + nums[right]
            if abs(tmp - target) < res:
                res = abs(tmp - target)
                r = nums[i] + nums[left] + nums[right]
            if tmp > target:
                left += 1
            elif tmp < target:
                right -= 1
            else:
                return target

    return r
'''
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
思路：首先想到的是行里发现有0 的话那么，这一行肯定是首先需要全都变为 0 的
然后 列变为0 但是在继续判断是会因为  之前这行的某一个 数字因为其他行的影响为0，而误删掉这一整行
所以可以 用一个辅助数组，来记录那一列需要删除，而不要着急 遇到0就删除一整行在这一行每个索引遍历完后再
删除这一行，最后遍历辅助数组 删除相应的列就好

如果不用辅助数组 可以用 矩阵第一行来记录
'''


def setZeroes(matrix):
    rFlag = False
    for i in range(len(matrix)):
        flag = False
        for j in range(len(matrix[0])):
            if i == 0 and matrix[i][j] is 0:
                rFlag = True
            if matrix[i][j] is 0:
                flag = True
                matrix[0][j] = 0
        if flag and i > 0:
            matrix[i] = [0 for i in range(len(matrix[0]))]
    for x in range(len(matrix[0])):
        if matrix[0][x] is 0:
            for y in range(len(matrix)):
                matrix[y][x] = 0
    if rFlag:
        matrix[0] = [0 for i in range(len(matrix[0]))]
    print(matrix)


def groupAnagrams(strs):
    if len(strs) is 0:
        return []
    dp = [[strs[0]]]

    for i in range(1, len(strs)):
        # l = list(strs[i])
        l = sorted(strs[i])
        flag = False
        for j in range(len(dp)):
            r = sorted(dp[j][0])
            if l == r:
                flag = False
                dp[j].append(strs[i])
                break
            else:
                flag = True

        if flag:
            dp.append([strs[i]])
    return dp


'''
字谜分组
维护一个映射 ans : {String -> List}，其中每个键
ext{K}K 是一个排序字符串，每个值是初始输入的字符串列表，排序后等于 ext{K}K。
在 Java 中，我们将键存储为字符串，例如，code。 在 Python 中，我们将键存储为散列化元组，
例如，('c', 'o', 'd', 'e')。
'''


def groupAnagramsOne(strs):
    ans = collections.defaultdict(list)

    for i in strs:
        ans[str(sorted(i))].append(i)

    r = []
    for i in ans.values():
        r.append(i)
    return r

def lengthOfLongestSubstring(s):
    '''
    无重复字符的最长子串
    维持一个滑动窗口
    有三种情况需要考虑
    一、当新加入的字符 不存在之前的子序列中的时候那么这个在字符就可以加入子串中
    二、当新加入的字符已经存在于子串中的时候，而且重复的位置在子串的第一位的时候，可以删除第一位的字符，并在结尾加入当前字符
    三、当新加入的字符已经存在于子串中的时候，而且重复的位置不在子串的第一位的时候，需要删除重复位置之前的子串
    并新加入当前字符
    最后需要有一个 值记录滑动窗口的最大值
    '''

    if len(s) == 0:
        return 0
    tmp = [s[0]]
    t = 1
    for i in range(1, len(s)):
        if tmp.count(s[i]) == 0:
            tmp.append(s[i])
            if len(tmp) > t:
                t = len(tmp)
        elif tmp.index(s[i]) != 0:
            tmp = tmp[tmp.index(s[i]) + 1:]
            tmp.append(s[i])
        else:
            if len(tmp) > t:
                t = len(tmp)
            tmp.remove(s[i])
            tmp.append(s[i])
    return t


def longestPalindrome(s):
    '''
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000
    Manacher's
    https://www.cnblogs.com/mini-coconut/p/9074315.html
    '''
    if len(s) == 0:
        return ""

    l = ["#"]
    for i in range(len(s)):
        l.append(s[i])
        l.append("#")
    r = [0 for i in range(len(l))]
    max = 0
    left = 0
    index = 0
    maxLen = 0
    for i in range(1, len(l)):
        r[i] = 1 if i > max else min(r[2 * index - i], max - i)  # min为了防止越界
        while i + r[i] < len(l) and i - r[i] >= 0 and l[i + r[i]] == l[i - r[i]]:
            r[i] += 1  # 寻找回文串
        if i + r[i] > max:  # 如果当前位置的回文串最右边的索引位置大于当前记录的最大値
            index = i  # 更新最大边界中心索引位置
            max = i + r[i] - 1  # 跟新最大边界索引位置
        if r[i] - 1 > maxLen:  # 更新回文串长度最大値
            maxLen = int(r[i] - 1)
            left = int((i - r[i] + 1) / 2)
    print(r)
    return s[left:left + maxLen]

def increasingTriplet(nums):
    '''
     递增的三元子序列
    给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

    数学表达式如下:

    如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
    使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
    '''
    if len(nums) < 3:
        return False
    h, k = 2 << 30, 2 << 30
    for i in nums:
        if h >= i: #如果当前值小于h则更新h,
            h = i
        elif k >= i: #如果当前值大于h但是小于k
            k = i
        else:       #如果当前值大于k就说明 已经找到三个数按大小顺序排列直接返回True
            return True
    return False


if __name__ == '__main__':
    print(increasingTriplet([1, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 20]))
