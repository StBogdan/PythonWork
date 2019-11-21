class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        steck = []
        indexStack = []
        for i, x in enumerate(s):
            if x == '(':
                steck.append(x)
                indexStack.append(i)
            elif x == ')':
                if steck and steck[-1] == '(':
                    steck.pop()
                    indexStack.pop()
                else:
                    steck.append(x)
                    indexStack.append(i)

        return "".join(letr for i, letr in enumerate(s) if i not in indexStack)


if __name__ == '__main__':
    folder =  "a)b(c)d"  #"lee(t(c)o)de)"
    sol = Solution()
    print(f"Ans: {sol.minRemoveToMakeValid(folder)}")