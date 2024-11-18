class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k>0:
            k = abs(k)
            l1 = []
            for i in range(len(code)):
                l1.append(0)
                for j in range(k):
                    if i+j+1 < len(code):
                        l1[i] = l1[i] + code[i+j+1]
                    else:
                        l1[i] = l1[i] + code[i+j+1-len(code)]
            code = l1
        elif k<0:
            k = abs(k)
            l1 = []
            for i in range(len(code)): #4
                l1.append(0)
                for j in range(k): #2
                    if i-j-1 < 0:
                        l1[i] = l1[i] + code[i-j-1+len(code)]
                    else:
                        l1[i] = l1[i] + code[i-j-1]
            code = l1
        else:
            for i in range(len(code)):
                code[i] = 0
        return code
                        
