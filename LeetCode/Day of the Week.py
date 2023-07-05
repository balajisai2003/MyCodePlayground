
class Solution:
    def __init__(self):
        self.weeks = {
            0 : "Sunday" ,
            1 : "Monday" ,
            2 : "Tuesday" ,
            3 : "Wednesday" ,
            4 : "Thursday" ,
            5 : "Friday" ,
            6 : "Saturday"
        }

        self.months = {
            1 : 0 ,
            2 : 3 ,
            3 : 3 ,
            4 : 6 ,
            5 : 1 ,
            6 : 4 ,
            7 : 6 ,
            8 : 2 ,
            9 : 5 ,
            10 : 0 ,
            11 : 3 ,
            12 : 5 
        }
        self.century = {
            19 : 0,
            20 : 6,
            21 : 4
        }
    def leapyear(year):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        dayval = day+self.months[month]+self.century[year//100]+year%100+(year%100)//4
        if self.leapyear(year) and (month==1 or month ==2):
            return self.weeks[dayval%7-1]
        else:
            return self.weeks[dayval%7]
