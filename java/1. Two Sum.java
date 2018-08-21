//java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int results[] = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                Integer sum = nums[i] + nums[j];//此处须要将sum定义为Integer，否则无法使用equals函数，因int不是java基本类型
                if (sum.equals(target)){
                    results[0] = i;
                    results[1] = j;
                    return results;
                }
            }
        }
        return results;
    }
}
