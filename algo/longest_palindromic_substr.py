class SlidingWindowImplSolver:
    """ Sliding window implementation
        1. Get length of string, palindrome can only be string with length 2 -> N.
        2. Traverse sliding window of length N -> 2 and get substring.
        3. For every slide, check if substring is palindrome.
        4. If substring is palindrome, return it immediately, this already ensures that this is the first
           and longest palindrome.
        5. If there's no palindrome, we just return None.
    """ 

    def solve(self, string: str) -> str | None:
        for n in range(len(string), 1, -1):
            start = 0
            end = n

            while (end <= len(string)):
                substr = string[start:end]

                if self._is_palindrome(substr):
                    return substr
            
                start += 1
                end += 1

        return None

    def _is_palindrome(self, string: str) -> bool:
        return string == string[::-1]


def test_longest_palindrome_substring():
    INPUT_OUTPUT_MAP = [
        ["babad", "bab"],
        ["crisis", "isi"],
        ["civic", "civic"],
        ["redivider", "redivider"],
        ["abcdefg", None],
        ["cheese", "ese"]
    ]

    solver = SlidingWindowImplSolver()

    count = 0

    for in_str, out_str in INPUT_OUTPUT_MAP:
        output = solver.solve(in_str)
        if output == out_str:
            print(f"[{count + 1}] PASSED - Input: {in_str}, Output: {output}, Expected: {out_str}")
        else:
            print(f"[{count + 1}] FAILED - Input: {in_str}, Output: {output}, Expected: {out_str}")
        
        count += 1


if __name__ == "__main__":
    test_longest_palindrome_substring()