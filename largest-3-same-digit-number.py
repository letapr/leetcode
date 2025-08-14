class Solution:
    def largestGoodInteger(self, num: str) -> str:
        out = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2] and num[i] > out:
                out = num[i:i+3]
        return out

if __name__ == "__main__":
    solution = Solution()
    print(solution.largestGoodInteger("6777133339"))
    print(solution.largestGoodInteger("2300019"))
    print(solution.largestGoodInteger("42352338"))
