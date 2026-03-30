class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}

        for i in s:
            if i not in dic_s.keys():
                dic_s[i] = 0
            dic_s[i] += 1
        
        for i in t:
            if i not in dic_t: # = if i not in dic_t.keys():
                dic_t[i] = 0
            dic_t[i] += 1

        return dic_s == dic_t
        '''
        python字典可以直接比较, {'a': 1, 'b': 2} == {'b': 2, 'a': 1}
        for i in dic_s.keys():
            if dic_s[i] != dic_t[i]:
                return False
        '''
        