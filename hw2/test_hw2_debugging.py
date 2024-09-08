import hw2_debbugging
import pytest

@pytest.mark.parametrize("arr, expected_result", [
    ([2,3,1,4], [1,2,3,4]),
    ([2,3,1,4], [1,2,3,4]),
    ([1], [1]),
    ([], [])
])
def test_hw2_debugging_sort(arr, expected_result):
    result = hw2_debbugging.mergeSort(arr=arr)
    assert result == expected_result
