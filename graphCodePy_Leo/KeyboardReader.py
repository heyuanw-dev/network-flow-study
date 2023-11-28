import sys

class KeyboardReader:
    EOI_INT = float('inf')
    EOI_DOUBLE = float('inf')
    EOI_STRING = "END_OF_INFO_1234"
    ERROR_INT = float('-inf')
    ERROR_DOUBLE = float('-inf')
    ERROR_STRING = "I/O_ERROR_1234"
    ERROR_MESSAGES = True

    @staticmethod
    def read_int():
        try:
            s = input()
            return int(s.strip())
        except ValueError:
            if KeyboardReader.ERROR_MESSAGES:
                print("Bad input: enter digits without decimal point")
            return KeyboardReader.ERROR_INT
        except EOFError:
            return KeyboardReader.EOI_INT

    @staticmethod
    def read_double():
        try:
            s = input()
            return float(s.strip())
        except ValueError:
            if KeyboardReader.ERROR_MESSAGES:
                print("Bad input: enter digits only")
            return KeyboardReader.ERROR_DOUBLE
        except EOFError:
            return KeyboardReader.EOI_DOUBLE

    @staticmethod
    def read_string():
        try:
            return input()
        except EOFError:
            return KeyboardReader.EOI_STRING

# Example usage
KeyboardReader.ERROR_MESSAGES = False

# Reading an integer
print("Enter an int")
while True:
    i = KeyboardReader.read_int()
    if i == KeyboardReader.EOI_INT:
        print("EOI")
        break
    elif i == KeyboardReader.ERROR_INT:
        print("ERROR")
        continue
    else:
        print(f"{i} entered")

# Similar loops can be used for read_double and read_string
