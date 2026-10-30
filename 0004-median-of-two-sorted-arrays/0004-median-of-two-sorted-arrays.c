
double findMedianSortedArrays(int* nums1, int m, int* nums2, int n) {
    // Always perform binary search on the smaller array
    if (m > n) {
        return findMedianSortedArrays(nums2, n, nums1, m);
    }

    int low = 0, high = m;
    int half = (m + n + 1) / 2;

    while (low <= high) {
        int i = (low + high) / 2;
        int j = half - i;

        int left1 = (i == 0) ? -2147483647 : nums1[i - 1];
        int right1 = (i == m) ? 2147483647 : nums1[i];

        int left2 = (j == 0) ? -2147483647 : nums2[j - 1];
        int right2 = (j == n) ? 2147483647 : nums2[j];

        if (left1 <= right2 && left2 <= right1) {
            if ((m + n) % 2 == 0) {
                int maxLeft = (left1 > left2) ? left1 : left2;
                int minRight = (right1 < right2) ? right1 : right2;

                return ((double)maxLeft + minRight) / 2.0;
            } else {
                return (left1 > left2) ? left1 : left2;
            }
        }
        else if (left1 > right2) {
            high = i - 1;
        }
        else {
            low = i + 1;
        }
    }

    return 0.0;
}