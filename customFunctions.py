class customFunctions:
    def myAtoi(self, s: str) -> int:
        sign = 1
        leadingSpaceFlag = True
        decimalFlag = False
        digits = 0
        decimalDigits = 0
        for i in range(len(s)):
            c = s[i]
            
            if  digits > 0 and (c == ' ' or c == '+' or c == '-' or c.isalpha()):
                break;
            
            if leadingSpaceFlag == True and c == ' ':
                continue
            leadingSpaceFlag = False
            
            if c == '+' or c == '-':
                if c == '-' and s != -1 and s[i+1].isdigit():
                    sign = -1
                continue
                
            if c == '.' and digits > 0:
                decimalFlag = True
            
            if (c.isdigit()):
                if digits == 0:
                    if decimalFlag == False:
                        digits += 1
                        digitC = int(c)
                        res = digitC * sign
                        resDeci = 0
                    else:
                        digits += 1
                        decimalDigits += 1
                        resDeci = int(c) * sign
                else:
                    if decimalFlag == False:
                        digits += 1
                        res = (res * pow(10, digits-1)) + (int(c)*sign)
                    else:
                        digits += 1
                        decimalDigits += 1
                        resDeci =  (resDeci * pow(10, decimalDigits-1)) + int(c)
        
        finRes = float(res) + ((float(resDeci) / pow(10, decimalDigits)) if resDeci > 0 else 0.0)*sign
        return round(finRes)
    def __init__(self) -> void:
	s = "     -43.56 +.34 m.oeeeee         "
	print(self.myAtoi(s))

                