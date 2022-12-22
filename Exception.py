class MyEexception(Exception):
    """General exception class"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Error: {self.message}"


class ExceptionEmptyString(MyEexception):
    """Exception. Сhecking for an empty string """
    pass


class GetNum:
    def check_empty_string(self, string):
        if string == '': raise ExceptionEmptyString("You cannot enter an empty string")
        return string

    def get_num(self):
        while True:
            try:
                return float(self.check_empty_string(input("Input fractional number => ")))
            except ExceptionEmptyString:
                print("You cannot enter an empty string. Try again =>")
            except ValueError:
                print("The number is entered incorrectly. Try again =>")
                continue


n = GetNum()
num = n.get_num()
print(num)
