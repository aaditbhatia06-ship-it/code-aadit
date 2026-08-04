class Solution:
    def reverseString(self, s: List[str]) -> None:
      stack = []
      for i in range(len(s)):
        stack.append(s[i])
      for i in range(len(s)):
        s[i] = stack.pop()

     