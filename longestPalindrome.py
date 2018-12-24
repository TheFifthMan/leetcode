# 暴力破解法
def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1 or len(s) == 0:
            return s
        arrs = ""
        for i in range(0,len(s)):
            temps = ""
            temps = temps + s[i] 
            for j in range(i+1,len(s)):
                #print(arrs)
                temps = temps + s[j] 
                
                if temps[::-1] == temps and len(temps) >= 1 and len(arrs) < len(temps):
                    arrs = temps
        if len(arrs) == 0:
            arrs = s[0]        
                
        return ''.join(arrs)
'''
a   = 1

ac  - 1
aa  - 2

aba = 3
aab = 2
abc = 1

abcd = 1
aabc = 2
acac = 3
abba = 4



'''

    
    


if __name__ == "__main__":
    print(longestPalindrome("a"))
    print(longestPalindrome("babad"))
    print(longestPalindrome("ac"))
    print(longestPalindrome(""))
    

    