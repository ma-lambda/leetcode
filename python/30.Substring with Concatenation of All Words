class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        lws = len(''.join(words)) # the length of all words
        ls = len(s) # the length of s
        if  lws > ls or len(words) < 1 or ls == 0:
            return []
        lw = len(words[0]) # the length of word
        for i in range(0, ls - lws + 1):
            words_temp = words[:]
            for j in range(i, i + lws, lw):
                word = s[j:j + lw]
                if word not in words_temp:
                    break
                else:
                    index = words_temp.index(word)
                    del words_temp[index]
                if not words_temp:
                    res.append(i)
                    break
        return res
