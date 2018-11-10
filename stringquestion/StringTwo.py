# -*- coding: UTF-8 -*-
import collections


def threeSum(nums):
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

    r =[]
    for i in ans.values():
        r.append(i)
    return r



if __name__ == '__main__':
    print(groupAnagramsOne(["eat", "tea", "tan", "ate", "nat", "bat"]))
