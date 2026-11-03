class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append(f"{len(word)}#{word}")
        encoded_string = "".join(parts)
        return encoded_string



    """ n2 solution
    def decode(self, s: str) -> List[str]:
        result = []
        while s:
            length, s = s.split("#", 1)
            n = int(length)
            result.append(s[:n])
            s = s[n:]
        return result
    """
    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            j = i 
            # get digits of count
            while s[j] != "#":
                j += 1
            # get the length
            length = int(s[i:j])
            # get the word of length size
            word = s[j + 1 : j + 1 + length]
            # add in results words
            words.append(word)
            i = j + 1 + length
        return words
                




        
