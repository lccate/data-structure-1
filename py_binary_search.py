# cate
# 19.3.26
# 用python实现二分查找


def binary_search(search_list, target):
    left = 0
    right = len(search_list) - 1
    while left <= right:
        mid = (left + right) / 2
        if search_list[mid] < target:
            left = mid + 1
            continue
        if search_list[mid] == target:
            return mid
        if search_list[mid] >= target:
            right = mid - 1
    return None


search_list = [1, 6, 3, 5, 9, 8]
print(binary_search(search_list, 7))
print(binary_search(search_list, 3))
print(binary_search(search_list, 5))
