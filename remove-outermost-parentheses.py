class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        depth = 0
        i = -1
        arr = []
        for p in S:
            if depth == 0 and p == "(":
                i += 1
                arr.append("")
            if p == "(":
                depth += 1
            else:
                depth -= 1

            arr[i] += p

        temp = ""
        for x in arr:
            temp += x[1:-1]

        return temp