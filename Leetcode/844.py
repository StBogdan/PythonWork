class Solution:

    @staticmethod
    def text_editorize(raw_input: str):
        buff_S=[]
        for c in raw_input:
            if c == "#": 
                if buff_S: # Can't pop if no elems
                    buff_S.pop()
            else:
                buff_S.append(c)
        return buff_S

    def backspaceCompare(self, S:str, T:str) -> bool:
        r1 = "".join(self.text_editorize(S))
        r2 = "".join(self.text_editorize(T))
        print(r1 + " -- " + r2)
        return r1 == r2
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.backspaceCompare("a##c", "##a#c"))
    print(sol.backspaceCompare("ab#c", "ad#c"))
