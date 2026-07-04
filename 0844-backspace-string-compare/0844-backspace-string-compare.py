class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for ch in s:
            if ch == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(ch)

        s = "".join(stack1)

        for ch in t:
            if ch == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(ch)

        t = "".join(stack2)

        if s == t:
            return True
        else:
            return False
