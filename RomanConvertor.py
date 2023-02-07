
class RomanConvertor() :
    
    def convert(arabicNumber):
                
        match arabicNumber:
            case 1:
                return "I"
            case 2:
                return "II"
            case 3:
                return "III"
            case _:
                return "WTF DUDE"
            
        # match arabicNumber:
        #     case 1, 2, 3:
        #         return "I"*arabicNumber
        #     case _:
        #         return "WTF DUDE"
            
        
