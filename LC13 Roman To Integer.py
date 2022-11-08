def romanToInt(self, s: str) -> int:
    
    values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV":4, "IX":9, "XL":50, "XC":90, "CD":500, "CM":900}
    symbols = []
    subtracted_amount = 0 # amount we need to remove
    total_amount = 0 # raw total
    tmp_1 = 4000
    for symbol in s:
        symbols.append(symbol)  
    for i in range(len(symbols)):
        total_amount += values[symbols[i]]
        if values[symbols[i]] > tmp_1:
            subtracted_amount += 2 * (values[symbols[i-1]]) # amount that needs to be subtracted      
        tmp_1 = values[symbols[i]] # previous value amount
    return total_amount - subtracted_amount

print(romanToInt(0, "MCMXCIV"))