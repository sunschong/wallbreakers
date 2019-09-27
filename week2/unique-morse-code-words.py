class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        code = {alpha[i]:morse[i] for i in range(len(alpha))}
        result = dict()
        for w in words:
            curr = ''
            for x in w:
                curr += code[x]
            result[curr] = 0
        return len(result.keys())