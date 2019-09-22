class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #all caps, all lowercase, or first captial
        if word == word.upper() or word == word.lower():
            return True
        else:
            if word[0].islower():
                return False
            for i in range(1, len(word)):
                if word[i].isupper():
                    return False
            return True