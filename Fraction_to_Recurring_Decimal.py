class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = "" if numerator * denominator > 0 else "-"
        numerator,denominator = abs(numerator),abs(denominator)

        integer_part = numerator//denominator
        remainder = numerator % denominator

        result = [sign + str(integer_part)]
        if remainder == 0:
            return ''.join(result)

        result.append(".")
        remainders = {}
        repeat_start = None
        position = len(result)
        
        while remainder > 0:
            if remainder in remainders:
                repeat_start = remainders[remainder]
                break
            remainders[remainder] = position
            position += 1

            digit,remainder = divmod(remainder * 10, denominator)
            result.append(str(digit))
        
        if repeat_start is not None:
            result.insert(repeat_start, "(")
            result.append(")")
        return ''.join(result)