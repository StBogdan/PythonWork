class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        lb = self.get_next_seq(low, False)
        ans_arr =[]

        while lb <= high:
            if lb >= low:
                ans_arr.append(lb)
            lb = self.get_next_seq_better(lb)
        return ans_arr


    @staticmethod
    def get_next_seq(prev, is_curn_perf=True):
        str_prev = str(prev)
        n = len(str_prev)
        fd = int(str_prev[0])

        curn = 0
        if (is_curn_perf and '9' in str_prev) or fd + n > 10:
            n += 1
            fd = 1
        else:
            if is_curn_perf:
                fd += 1

        for i in range(n-1, -1, -1):
            curn += fd*(10**i)
            fd += 1

        return curn

    @staticmethod
    def get_next_seq_better(prev, is_curn_perf=True):
        ld = prev % 10
        if is_curn_perf and ld == 9:
            return int("".join(map(str, range(1, len(str(prev))+2))))
        else:
            return int(str(prev)[1:])*10 + (ld+1)
