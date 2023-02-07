
class RomanConvertor() :
    arabicNumber = 5
    
    def convert(self, arabicNumber): 
        
        match arabicNumber:
            case 1:
                return "I"
            case 2:
                return "II"
            case 3:
                return "III"
            case _:
                return "WTF DUDE"
            
        
