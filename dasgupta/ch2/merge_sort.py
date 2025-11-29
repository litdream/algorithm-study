#!/usr/bin/env python3

def merge_sort(nums: list) -> list:
    """Implement merge sort algorithm.

    Args:
        nums: List of comparable elements to be sorted

    Returns:
        A new list:  sorted nums in ascending order

    Example:
        >>> merge_sort([5, 2, 8, 1, 9])
        [1, 2, 5, 8, 9]
        >>> merge_sort([])
        []
        >>> merge_sort([1])
        [1]
    """

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    # Conquer: recursively sort each half
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Combine: merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left: list, right: list) -> list:
    """Merge two **sorted** lists into a single sorted list.
    Runtime:  O(n)

    Args:
        left: First sorted list
        right: Second sorted list

    Returns:
        A **new** sorted list containing all elements from both input lists

    Example:
        >>> merge([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """

    result = []
    i = j = 0

    # Compare elements from left and right, adding the smaller one to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from left
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from right
    while j < len(right):
        result.append(right[j])
        j += 1

    return result
