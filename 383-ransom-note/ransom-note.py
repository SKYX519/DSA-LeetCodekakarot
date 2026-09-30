class Solution:
    def canConstruct(self, ransomNote, magazine):
        count = [0] * 26

        for ch in magazine:
            count[ord(ch) - 97] += 1

        for ch in ransomNote:
            index = ord(ch) - 97

            if count[index] == 0:
                return False

            count[index] -= 1

        return True