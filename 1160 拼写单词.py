#给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
#假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
#注意：每次拼写（指拼写词汇表中的一个单词）时，chars 中的每个字母都只能用一次。
#返回词汇表 words 中你掌握的所有单词的 长度之和。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        flag=0
        for w in words:
            for i in w:
                if w.count(i) <= chars.count(i):
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                ans+=len(w)
        return ans
