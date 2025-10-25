# src/algorithms.py
from __future__ import annotations
import random
from typing import List, Tuple

def min_max_divide_conquer(arr: List[float]) -> Tuple[float, float]:
    """
    Return (min, max) of arr using a recursive divide-and-conquer approach.
    Complexity: O(n) time, O(log n) stack space.

    Raises:
        ValueError: if arr is empty.
    """
    if not arr:
        raise ValueError("Array must not be empty.")

    def rec(lo: int, hi: int) -> Tuple[float, float]:
        # Base: one element
        if lo == hi:
            return arr[lo], arr[lo]
        # Base: two elements (one comparison)
        if hi == lo + 1:
            if arr[lo] < arr[hi]:
                return arr[lo], arr[hi]
            else:
                return arr[hi], arr[lo]
        # Recurse on halves, then combine
        mid = (lo + hi) // 2
        left_min, left_max = rec(lo, mid)
        right_min, right_max = rec(mid + 1, hi)
        return (left_min if left_min < right_min else right_min,
                left_max if left_max > right_max else right_max)

    return rec(0, len(arr) - 1)


def quick_select(arr: List[float], k: int) -> float:
    """
    Return the k-th smallest element (1-based) from an unsorted list using Quickselect.
    Average complexity: O(n). Worst-case: O(n^2) (mitigated by random pivots).
    Does not mutate the input list.
    
    Args:
        arr: list of numbers
        k: 1-based index of the order statistic (1 <= k <= len(arr))
    """
    n = len(arr)
    if n == 0:
        raise ValueError("Array must not be empty.")
    if not (1 <= k <= n):
        raise ValueError(f"k must be in [1, {n}], got {k}.")

    a = list(arr)  # work on a copy
    target = k - 1

    def partition(lo: int, hi: int, p_idx: int) -> int:
        # Lomuto partition using pivot at hi
        a[p_idx], a[hi] = a[hi], a[p_idx]
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        return i

    lo, hi = 0, n - 1
    while True:
        p_idx = random.randint(lo, hi)  # randomized pivot
        pivot_final = partition(lo, hi, p_idx)
        if pivot_final == target:
            return a[pivot_final]
        if target < pivot_final:
            hi = pivot_final - 1
        else:
            lo = pivot_final + 1