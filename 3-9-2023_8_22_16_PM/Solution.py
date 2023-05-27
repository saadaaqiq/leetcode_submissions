# https://leetcode.com/problems/encode-and-decode-strings

class Codec:
    def encode(self, strs: List[str]) -> str:
        res_arr = []
        for s in strs:
            for c in s:
                if c in ["-", "\\"]:
                    res_arr.append("\\")
                res_arr.append(c)
            res_arr.append("-")
        return "".join(res_arr)

    def decode(self, s: str) -> List[str]:
        res = []
        cur = []
        escape = False
        for c in s:
            if c == "\\":
                if escape:
                    cur.append(c)
                    escape = False
                else:
                    escape = True
            elif c == "-":
                if escape:
                    cur.append(c)
                    escape = False
                else:
                    res.append("".join(cur))
                    cur = []
            else:
                cur.append(c)
        return res



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))