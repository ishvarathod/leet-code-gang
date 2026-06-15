def findMedianSortedArrays( nums1: list[int], nums2: list[int]) -> float:
  
    return


def main():
    nums1 = [1,2]
    nums2 = [3,4]


    merged = nums1 + nums2

    n = len(merged)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if merged[j] > merged[j + 1]:
                merged[j], merged[j + 1] = merged[j + 1], merged[j]
                swapped = True
        if not swapped:
            break  


    if len(merged) % 2 == 0:
      index = len(merged) // 2
      median = (merged[index] + merged[index - 1]) / 2
     

    else:
        index = len(merged) // 2
        median = merged[index]
    
    return median


if __name__ == "__main__":
    main()