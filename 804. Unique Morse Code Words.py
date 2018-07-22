class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        mos={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        
        ans=[]
        s_mos=''
        for word in words:
            for word_d in word:
                s_mos=s_mos+mos[word_d]
            
            if s_mos not in ans:
                ans.append(s_mos)
            s_mos=''
        return len(ans)