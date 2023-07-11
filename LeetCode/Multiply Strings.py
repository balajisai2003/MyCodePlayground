
class Solution:
    def __init__(self) -> None:
        self.dic = {
                        "1":1,
                        "2":2,
                        "3":3,
                        "4":4,
                        "5":5,
                        "6":6,
                        "7":7,
                        "8":8,
                        "9":9,
                        "0":0,
                        1:"1",
                        2:"2",
                        3:"3",
                        4:"4",
                        5:"5",
                        6:"6",
                        7:"7",
                        8:"8",
                        9:"9",
                        0:"0"
                    }
    def strTOint(self,num:str) -> int:
        n = 0
        for i in num:
            n = n*10 + self.dic[i]
        return n
    def intTOstr(self,num:int) -> str:
        n = ""
        while num>0:
            n+=self.dic[int(num%10)]
            num /= 10
        return n
    def multiply(self, num1: str, num2: str) -> str:
        return self.intTOstr(self.strTOint(num1)*self.strTOint(num2))
        
    
obj = Solution()

print(obj.multiply("23","24"))