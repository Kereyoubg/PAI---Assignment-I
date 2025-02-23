def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) < len(nums2):
        shorter = nums1
        longer = nums2
    else:
        shorter = nums2
        longer = nums1
    total_length = len(shorter) + len(longer)
    half_length = total_length // 2

    left_pointer = 0
    right_pointer = len(shorter) - 1
    while True:
        i = (left_pointer + right_pointer) // 2
        j = half_length - i - 2

        if i >= 0:
            left_shorter = shorter[i]
        else:
            left_shorter = float('-infinity')

        if i + 1 < len(shorter):
            right_shorter = shorter[i + 1]
        else:
            right_shorter = float('infinity')

        if j >= 0:
            left_longer = longer[j]
        else:
            left_longer = float('-infinity')

        if j + 1 < len(longer):
            right_longer = longer[j + 1]
        else:
            right_longer = float('infinity')

        # Partition is correct
        if left_shorter <= right_longer and left_longer <= right_shorter:
            # Odd total length
            if total_length % 2:
                return min(right_shorter, right_longer)
            # Even total length
            return (max(left_shorter, left_longer) + min(right_shorter, right_longer)) / 2
        elif left_shorter > right_longer:
            right_pointer = i - 1
        else:
            left_pointer = i + 1

nums1 = [1, 3]
nums2 = [2]

print(find_median_sorted_arrays(nums1, nums2))
