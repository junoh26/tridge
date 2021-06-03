# Question 2
# I assumed that the digits passed into Transformer constructor are ordered in ascending ascii value
# EX: base5('ABC12') -> 'A' would be 0 in base 10 and '2' would be 4 in base 10
class Transformer(object):
    decimal_digits = '0123456789'

    def __init__(self, digits):
        self.digits = digits

    def from_decimal(self, i):
        return self._convert(i, self.decimal_digits, self.digits)

    def to_decimal(self, s):
        return int(self._convert(s, self.digits, self.decimal_digits))

    def _convert(self, number, fromdigits, todigits):
        # base 10 num -> base N string
        if fromdigits == "0123456789":
            # construct dict of decimal val -> char
            dic = {}
            base = len(todigits)
            for i in range(base):
                dic[i] = todigits[i]
            
            digits = []
            while number > 0:
                digit = number % base
                digits.append(todigits[digit])
                number = int(number / base)

            return "".join(digits[::-1])
        # base N string -> base 10 num
        else:
            # construct dict of char -> decimal val
            dic = {}
            base = len(fromdigits)
            for i in range(base):
                dic[fromdigits[i]] = i
            power = 1
            num = 0

            for j in range(len(number)-1, -1, -1):
                # convert string digit into decimal integer
                val = dic[number[j]]
                # val must be lower than base
                if val >= base:
                    raise ValueError("invalid number")
                num += val * power
                power *= base

            return num

# test cases
base20 = Transformer("0123456789abcdefghij")
assert base20.from_decimal(1234) == "31e"
assert base20.to_decimal("31e") == 1234

binary_transformer = Transformer('01')
assert binary_transformer.from_decimal(12) == "1100"
assert binary_transformer.to_decimal("1100") == 12

base62_transformer = Transformer("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz")
assert base62_transformer.from_decimal(250) == "EC"
assert base62_transformer.to_decimal("EC") == 250