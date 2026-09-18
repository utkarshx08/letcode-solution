class Solution:
    def toLowerCase(self, s: str) -> str:
        hello = ""

        for ch in s:
            if 'A' <= ch <= 'Z':
                hello += chr(ord(ch) + 32)
            else:
                hello += ch

        return hello
        