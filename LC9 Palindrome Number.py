


def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        number = []
        
        for digit in x_str:
            number.append(digit)
        
        if x % 2 != 0: #odd
            split_digit = (len(x_str) // 2) + 1
            odd_halves = x_str.split(number[split_digit])
            print (odd_halves)
            # if int(odd_halves[0]) == int(reversed(odd_halves[1])):
            #     return True
            # else:
            #     return False


        if x % 2 == 0: #even
            even_first_half = []
            even_second_half = []
            for i in range(0, (len(x_str)/2) - 1, 1):
                even_first_half.append(i)
            for j in range(len(x_str)/2, len(x_str), 1):
                even_second_half.append(j)
            if even_first_half == reversed(even_second_half):
                return True
            else:
                return False





isPalindrome(0, 121)