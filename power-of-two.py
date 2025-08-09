import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # log base 2 of n == integer
        try: 
            return math.log2(n).is_integer()
        except ValueError:
            return False



if __name__ == "__main__":
    solution = Solution()
    print(solution.isPowerOfTwo(0))
