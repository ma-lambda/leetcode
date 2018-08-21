class Solution {
    public int lengthOfLongestSubstring(String s) {
        String sub = "";
        int l = 0, maxL = 0;
        for (int i = 0; i < s.length(); i++) {
            if (sub.indexOf(s.charAt(i)) != -1) {
                sub += s.charAt(i);
                if (l > maxL)
                    maxL = l;
                sub = sub.substring(sub.indexOf(s.charAt(i)) + 1);
                l = sub.length();
            }
            else {
                sub += s.charAt(i);
                l += 1;
            }
        }
        if (l > maxL)
            maxL = l;
        return maxL;
    }
}
