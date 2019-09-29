class UmumFormattingServices():

    def FixedNumber(self, number):
        return "{0:.2f}".format(number)

    def NumberRange(self, number, count = 8):
        return str(number).zfill(count)