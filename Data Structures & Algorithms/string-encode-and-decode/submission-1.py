class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        parts = []
        for ch in strs:
            parts.append(f"{len(ch)}#{ch}")
        encoded_string = "".join(parts)
        return encoded_string



    def decode(self, s: str) -> List[str]:
        decoded_string = []
        while s:
            length, s = s.split("#", 1)
            n = int(length)
            decoded_string.append(s[:n])
            s = s[n:]
        return decoded_string
        
