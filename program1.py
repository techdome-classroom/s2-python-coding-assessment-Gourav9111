class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else None
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("(]"))


    



  

