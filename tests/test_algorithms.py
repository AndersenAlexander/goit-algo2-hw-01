# tests/test_algorithms.py
import pytest
from src.algorithms import min_max_divide_conquer, quick_select

def test_min_max_basic():
    arr = [3, 1, 5, 2, 9, 4]
    assert min_max_divide_conquer(arr) == (1, 9)

def test_min_max_edge_cases():
    assert min_max_divide_conquer([7]) == (7, 7)
    assert min_max_divide_conquer([2, -5]) == (-5, 2)
    assert min_max_divide_conquer([-1, -1, -1]) == (-1, -1)

def test_quick_select_basic():
    arr = [3, 1, 5, 2, 9, 4]
    assert quick_select(arr, 1) == 1
    assert quick_select(arr, 2) == 2
    assert quick_select(arr, 3) == 3
    assert quick_select(arr, 4) == 4
    assert quick_select(arr, 5) == 5
    assert quick_select(arr, 6) == 9

def test_quick_select_with_duplicates():
    arr = [5, 3, 3, 8, 1, 1, 7]
    # Sorted = [1,1,3,3,5,7,8]
    assert quick_select(arr, 1) == 1
    assert quick_select(arr, 2) == 1
    assert quick_select(arr, 3) == 3
    assert quick_select(arr, 5) == 5
    assert quick_select(arr, 7) == 8

def test_errors():
    with pytest.raises(ValueError):
        min_max_divide_conquer([])
    with pytest.raises(ValueError):
        quick_select([], 1)
    with pytest.raises(ValueError):
        quick_select([1,2,3], 0)
    with pytest.raises(ValueError):
        quick_select([1,2,3], 4)
