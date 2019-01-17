# -*- coding: UTF-8 -*-
def simplifyPath(path):
    """
    71. 简化路径
    思路：用栈处理问题 。
    将文件夹名 压入栈中
    :type path: str
    :rtype: str
    """
    path += "/"
    fd = ""  # 存储文件夹 和 ".\.."
    res = ""
    stack = []

    for i in path:
        if i == "/" and fd == "..":
            if stack:
                stack.pop()
            fd = ""
            continue
        elif i == "/" and fd == ".":
            fd = ""
            continue
        elif i == "/":
            if fd != "":
                stack.append(fd)
            fd = ""
            continue
        fd += i

    if not stack:
        return "/"
    while stack:
        res = res + "/" + stack.pop(0)

    return res

def removeDuplicates(nums):
    """
    80.删除排序数组中的重复项 II
    :type nums: List[int]
    :rtype: int
    """
    idx = 0
    while idx < len(nums):
        if idx < 2 or nums[idx] != nums[idx - 2]:
            idx += 1
        else:
            nums.pop(idx)
    return idx


if __name__ == '__main__':
    print(simplifyPath("/home//foo/"))