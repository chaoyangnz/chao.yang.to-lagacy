title: 'LeetCode #1 Two Sum'
date: 2016-02-03 22:10:25
tags: LeetCode
---

# Question
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

**Input**: numbers={2, 7, 11, 15}, target=9
**Output**: index1=1, index2=2

# Analysis
It's easy to think that we can use two loops to traverse this array, but its time complexity is O(n*n).

Now if we sorted this array and we get some important information about ordered numbers. And sorting can be ultilized to safely ignore some unnecessary comparisons.

# Solution
``` java
import java.util.Arrays;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int len = nums.length;
        if(len < 2) throw new IllegalArgumentException();
        int[] sorted = new int[len];
        // O(n)
        System.arraycopy(nums, 0, sorted, 0, len);
        // O(nlogn)
        Arrays.sort(sorted);

        int i=0;
        int j=len-1;
        // O(n)
        while(i<j) {
            int actual = sorted[j];
            int expect = target - sorted[i];
            if(actual == expect) return indices(nums, sorted[i], sorted[j]);
            if(actual > expect) --j;
            if(actual < expect) ++i;
        }

        return new int[2];
    }

    // retrieve the indices from the original number array
    private static int[] indices(int[] nums, int num1, int num2) {
        int len = nums.length;
        int[] arr = new int[2];
        int found = 0;
        for(int i=0; i < len && found < 2; ++i) {
            if(nums[i] == num1 || nums[i] == num2)  {
                arr[found] = i+1;
                ++found;
            }
        }
        return arr;
    }
}
```

# Submission & Judgement

[Submission in LeetCode](https://leetcode.com/submissions/detail/52575179/)

