class Solution:
    def romanToInt(self, s):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

<<<<<<< HEAD
        total = 00
=======
        total = 0
>>>>>>> refs/remotes/origin/main
        prev_value = 0

        for char in reversed(s):
            current_value = roman_values[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value

        return total

if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))
    print(sol.romanToInt("LVIII"))
    print(sol.romanToInt("MCMXCIV"))
