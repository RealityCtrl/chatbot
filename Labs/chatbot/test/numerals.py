class NumeralConverter:

    def handle_thousands(self, number):
        return 'M' * int(number // 1000)

    def handle_hundreds(self, number):
        hundreds = number % 1000
        if hundreds >= 900:
            return 'CM'
        elif hundreds < 500:
            if hundreds >= 400:
                return 'CD'
            else:
                return 'C' * int(hundreds // 100)
        else:
            return 'D' + 'C' * int((hundreds - 500) // 100)

    def handle_tens(self, number):
        hundreds = number % 1000
        tens = hundreds % 100
        if tens >= 90:
            return 'XC'
        elif tens < 50:
            if tens >= 40:
                return 'XL'
            else:
                return 'X' * int(tens // 10)
        else:
            return 'L' + 'X' * int((tens - 50) // 10)

    def handle_digits(self, number):
        hundreds = number % 1000
        tens = hundreds % 100
        digits = tens % 10
        if digits == 0:
            return ""
        if digits >= 9:
            return 'IX'
        elif digits < 5:
            if digits >= 4:
                return 'IV'
            else:
                return 'I' * digits
        else:
            return 'V' + 'I' * (digits - 5)

    def convert(self, number):

        if isinstance(number, str) or isinstance(number, float) or number <=0:
            return "Invalid number for conversion"
        numeral_string = ""
        if number >= 1000:
            numeral_string += self.handle_thousands(number)
        if (number >= 100):
            numeral_string += self.handle_hundreds(number)
        if (number >= 10):
            numeral_string += self.handle_tens(number)
        numeral_string += self.handle_digits(number)
        return numeral_string

