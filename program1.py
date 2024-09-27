class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
<<<<<<< HEAD

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else None
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

=======

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else None
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

>>>>>>> refs/remotes/origin/main
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("(]"))
<<<<<<< HEAD
=======


    



  
>>>>>>> refs/remotes/origin/main

